import re
import sys
import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import filedialog
import PySide2
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QBrush
from PySide2.QtWidgets import QApplication, QMainWindow
import ast
from Config import Config
from GraczSieciowyADlg import GraczSieciowyADlg
from GridModel import Colors
from WyborGryDlg import WyborGryDlg
from boardWidget import Ui_Form
from layout2 import Ui_MainWindow
from tcpClient import TcpClient
from tcpServer import TcpServer


# Grid ma wymiary (wymiar x wymiar x wymiar)
class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.read_config_json()
        self.setupUi(self)

        self.setup_new_game()

        self.tcpServer = TcpServer(1234, self.gotTcpServerData)
        self.tcpClient = TcpClient(1234, self.gotTcpClientData)

        self.tablica_1.enable(False)

        self.dlgGraczSieciowyA = None

        #self.setCentralWidget(self.tablica_1)
        #self.setCentralWidget(self.tablica_2)

        #self.setCentralWidget(self.centralwidget)

        # greenBrush = QBrush(Qt.green)
        # blueBrush = QBrush(Qt.blue)
        # blackPen = QPen(Qt.black)
        # blackPen.setWidth(5)

        self.new_game_button.clicked.connect(self.new_game)
        self.save_button.clicked.connect(self.save_state)
        self.load_button.clicked.connect(self.load_state)
        self.exit_button.clicked.connect(sys.exit)
        self.btReplay.clicked.connect(self.start_animation)
        self.undo_button.clicked.connect(self.undo)

        # self.exit_button.clicked.connect(sys.exit)
        # self.save_button.clicked.connect(self.plansza.save_state)
        # self.load_button.clicked.connect(self.plansza.load_state)

        # for x in range (rozmiarPlanszy) :
        #     for y in range(rozmiarPlanszy):
        #         hex = Hexagon(scene, x, y, size)
        #         pola.append([hex, x, y])

        #self.graphicsView_1.setScene(self.scene)


        # self.view = QGraphicsView(self.scene, self)
        # self.view.setGeometry(0, 0, 640, 520)
        # self.setWindowTitle("nazwa")
        # self.setGeometry(300, 200, 640, 520)    # (położenie okna x, położenie okna y, szerokość, wysokość)

        self.typGry = 0
        self.updateTypGry()
        self.show()

        self.animationStep = -1
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_tick)
        self.timer.start(1000)

    def setup_new_game(self):
        self.tablica_1 = Ui_Form(self.wymiar, "Gracz A:", "A", self)
        self.tablica_2 = Ui_Form(self.wymiar, "Gracz B:", "B", self)
        self.tablica_1.setupUi(self, 0)
        self.tablica_2.setupUi(self, 400)

        self.history = []
        self.history.clear()
        self.add_to_history()

    def update_step_info(self, p1, p2):
        self.lbStepInfo.setText(str(p1)+"/"+str(p2))

    def add_to_history(self):
        self.history.append( [ self.tablica_1.plansza.get_pola_copy(), self.tablica_2.plansza.get_pola_copy()])
        self.update_step_info(len(self.history), len(self.history))

    def movement(self, idGracza, typRuchu):
        print(idGracza, ":", typRuchu)

        self.add_to_history()

        if self.typGry == 0 or self.typGry == 1 :
            return

        self.tablica_1.enable(idGracza == "B")
        self.tablica_2.enable(idGracza == "A")

    def print(self, color, msg):
        print(color[0] + msg+ Colors.ENDC[0])
        self.teLog.append( color[1]  + msg )
        return

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Q:
            self.plansza.moveNWFull()
        if event.key() == Qt.Key_E:
            self.plansza.moveNEFull()
        if event.key() == Qt.Key_A:
            self.plansza.moveWFull()
        if event.key() == Qt.Key_D:
            self.plansza.moveEFull()
        if event.key() == Qt.Key_Z:
            self.plansza.moveSWFull()
        if event.key() == Qt.Key_C:
            self.plansza.moveSEFull()
        if event.key() == Qt.Key_N:
            self.plansza.new_game()

        if event.key() == Qt.Key_P:
            self.plansza.save_state()
        if event.key() == Qt.Key_L:
            self.plansza.load_state()

    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        super().mousePressEvent(event)
        self.tablica_1.mouse_pressed(event.x(),event.y())
        self.tablica_2.mouse_pressed(event.x(), event.y())

    def mouseReleaseEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        super().mouseReleaseEvent(event)
        self.tablica_1.mouse_released(event.x(),event.y())
        self.tablica_2.mouse_released(event.x(), event.y())

    def gotTcpClientData(self, data):
        return

    def gotTcpServerData(self, data):
        print("gotTcpServerData:",data)
        if self.dlgGraczSieciowyA != None :
            self.dlgGraczSieciowyA.close()
        self.tablica_1.enable(True)

    def updateTypGry(self):
        self.tablica_1.enable(False)
        self.tablica_2.enable(False)
        if self.typGry == 1 :
            self.tablica_1.enable(True)
        elif self.typGry == 2 :
            self.tablica_1.enable(True)
            self.tablica_2.enable(True)
        elif self.typGry ==3 :
            self.tcpServer.startListen()
            self.dlgGraczSieciowyA = GraczSieciowyADlg()
            self.dlgGraczSieciowyA.exec()
            self.dlgGraczSieciowyA = None
            #self.tablica_1.enable(True)

    def save_config_json(self, wymiar):
        configObj = Config()
        configObj.wymiar = wymiar
        text_file = open("config.json", "w")
        text_file.write(configObj.toJSON())
        text_file.close()

    def read_config_json(self):
        try:
            text_file = open("config.json", "r")
            json_str = text_file.read()
            #print(json_str)
            text_file.close()
            self.wymiar = int(re.sub("[^0-9]", "", json_str))
        except:
            print ( "nie udało się odczytać konfiguacji")
            self.wymiar = 3

    def new_game(self):
        dlgWyborGryDlg = WyborGryDlg(self)
        dlgWyborGryDlg.exec()
        self.typGry = dlgWyborGryDlg.typGry
        self.wymiar = dlgWyborGryDlg.wymiar()

        self.save_config_json(self.wymiar)

        self.updateTypGry()
        self.tablica_1.new_game(self.wymiar)
        self.tablica_2.new_game(self.wymiar)

        self.history = []
        self.history.clear()
        self.add_to_history()

    def save_state(self):
        root = tk.Tk()
        root.withdraw()

        file = filedialog.asksaveasfile(filetypes=[("Xml files", "*.xml")])

        xml_doc = ET.Element('root')
        product = ET.SubElement(xml_doc, 'wymiar').text = str(self.wymiar)
        product = ET.SubElement(xml_doc, 'tableAEnabled').text = str(self.tablica_1.enabled)
        product = ET.SubElement(xml_doc, 'tableBEnabled').text = str(self.tablica_2.enabled)
        product = ET.SubElement(xml_doc, 'typGry').text = str(self.typGry)
        product = ET.SubElement(xml_doc, 'saved_state').text = repr(self.history)

        tree = ET.ElementTree(xml_doc)
        tree.write(file.name, encoding='UTF-8', xml_declaration=True)
        # self.logFunction("\n"+self.print_prefix+"ZAPISANO")
        print("zapisano")

    def load_state(self):

        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename(filetypes=[("Xml files", "*.xml")])

        try:
            with open(file_path,'rt') as f:
                fileContent = f.read();
                sets = re.findall(r'<wymiar>(.*)</wymiar>', fileContent)
                self.wymiar = int(sets[0])
                sets = re.findall(r'(\[.*\])', fileContent)
                self.history = ast.literal_eval(sets[0])
            self.print( Colors.RED, "wczytano plik :"+file_path)
            length = len(self.history)
            self.print(Colors.RED, "wczytano ruchów:" + str(length))

            sets = re.findall(r'<tableAEnabled>(.*)</tableAEnabled>', fileContent)
            self.tablica_1.enable( sets[0] =="True")

            sets = re.findall(r'<tableBEnabled>(.*)</tableBEnabled>', fileContent)
            self.tablica_2.enable( sets[0] =="True")

            sets = re.findall(r'<typGry>(.*)</typGry>', fileContent)
            self.typGry = int(sets[0])

            self.tablica_1.new_game(self.wymiar)
            self.tablica_2.new_game(self.wymiar)
            self.tablica_1.plansza.set_pola_copy(self.history[length-1][0])
            self.tablica_2.plansza.set_pola_copy(self.history[length-1][1])
            self.tablica_1.create_scene()
            self.tablica_2.create_scene()

            self.update_step_info(len(self.history), len(self.history))

        except:
            self.print( Colors.RED, "Plik z zapisaną grą nie został znaleziony lub błąd odczytu!")


    #
    #
    # def mouseReleaseEvent(self, event):
    #     #super(Window, self).mouseReleaseEvent(event)
    #     delta_y = event.y() - self.tempy
    #     delta_x = event.x() - self.tempx
    #     vect_len = math.sqrt(delta_x**2+delta_y**2)
    #     angle = 180 + math.atan2(delta_y, -delta_x) * 180 / math.pi
    #     margin = 20
    #     if vect_len > 40:
    #         if angle > 360 - margin or angle < 0 + margin:
    #             self.plansza.moveEFull()
    #         if 60 - margin < angle < 60 + margin:
    #             self.plansza.moveNEFull()
    #         if 120 - margin < angle < 120 + margin:
    #             self.plansza.moveNWFull()
    #         if 180 - margin < angle < 180 + margin:
    #             self.plansza.moveWFull()
    #         if 240 - margin < angle < 240 + margin:
    #             self.plansza.moveSWFull()
    #         if 300 - margin < angle < 300 + margin:
    #             self.plansza.moveSEFull()

    def update_screen_to_history_step(self,idx):
        self.tablica_1.plansza.set_pola_copy(self.history[idx][0])
        self.tablica_2.plansza.set_pola_copy(self.history[idx][1])
        self.tablica_1.create_scene()
        self.tablica_2.create_scene()
        self.update_step_info(idx+1, len(self.history))

    def timer_tick(self):
        if self.animationStep == -1 :
            return
        self.update_screen_to_history_step(self.animationStep)
        self.animationStep+=1
        if self.animationStep == len(self.history) :
            print("AnimationStep2 ", self.animationStep)
            self.animationStep = -1
            self.update_step_info(len(self.history), len(self.history))

            self.tablica_1.enable(self.tablica1WasEnabled)
            self.tablica_2.enable(self.tablica2WasEnabled)

            self.new_game_button.setEnabled(True)
            self.save_button.setEnabled(True)
            self.load_button.setEnabled(True)
            self.undo_button.setEnabled(True)
            self.autoplay_button.setEnabled(True)

    def start_animation(self):
        self.tablica1WasEnabled = self.tablica_1.enabled
        self.tablica2WasEnabled = self.tablica_2.enabled

        self.tablica_1.enable(False)
        self.tablica_2.enable(False)

        self.new_game_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.load_button.setEnabled(False)
        self.undo_button.setEnabled(False)
        self.autoplay_button.setEnabled(False)

        self.animationStep = 0

    def undo(self):
        if len(self.history) > 1 :
            self.history.remove(self.history[-1])
            self.update_screen_to_history_step(len(self.history)-1)
            self.tablica_1.enable(not self.tablica_1.enabled)
            self.tablica_2.enable(not self.tablica_2.enabled)
            if len(self.history) == 1 :
                self.tablica_1.enable(True)
                self.tablica_2.enable(True)



if __name__ == '__main__':
    print("\nSterowanie: q, a, z, e, d, c")
    print("\nHistoria ruchów:")
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
