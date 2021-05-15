"""
Rozmiar planszy powinien być dynamiczny (ustawiany w opcjach), domyślny rozmiar to 3x3x3.
Przy implementacji planszy nie należy używać żadnych zewnętrznych bibliotek.
Klasa opisująca pojedyncze pole planszy/obiekt na planszy powinna dziedziczyć po QGraphicsItem (1 pkt).
Grę należy zaimplementować przy użyciu biblioteki PySide2 oraz komponentu QGraphicsScene.
Mechanika gry jest standardowa - sumują się obiekty o tej samej wartości (2 pkt).
Przy grze dwuosobowej gracze istnieje blokada ruchu - po wykonaniu ruchu przez drugiego gracza (B) dopiero odblokowuje
się możliwość robienia następnego ruchu i dopiero wtedy zaktualizowana zostaje plansza gracza B (2 pkt).
Historia gry musi być wyświetlana w konsoli. Użycie kolorowej konsoli (1 pkt). Wyświetlenie w konsoli i przekierowanie
konsoli na kontrolkę QTextEdit (2 pkt).

W okienku powinny znaleźć się dwie plansze (gracz A i gracz B - sieciowy), działające przyciski do sterowania planszą
gracza A, punktacja obu graczy (labele), przycisk nowa gra (czyszczenie planszy),
wyjście (zamknięcie okna i wszystkich procesów),
zapisz historię gry(wyświetlające okienko dialogowe z wyborem ścieżki do zapisu pliku xml),
emuluj (wyświetlający okienko dialogowe do wczytania pliku xml),
autorozgrywka (do późniejszej implementacji) (4 pkt).
Okienko powinno być wyposażone w pasek menu gdzie poza opcjami z przycisków znajdą się elementy takie jak opcje
(okienko dialogowe z opcjami: adres ip, port połączenia, rozmiar plansz), wyszukaj gracza w sieci lokalnej,
połącz z drugim graczem. Obsługa gestów myszy do sterowania planszą (2 pkt).
Wyświetlanie grafik zewnętrznych z zasobów qrc za pomocą QGraphisItem (1 pkt).
Jeśli macie jakieś pytania do zadania - co czwartek jestem dostępny na discordzie.

TODO:
* Drugie okienko
* punktacja
* nowa gra (done)
* zapisywanie do xml i wczytywanie (done)
* przyciski do sterowania
"""

import math
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PySide2.QtGui import QBrush, QPen, QPolygonF, QKeyEvent
from PySide2.QtCore import Qt, QPoint
import sys
import random
import xml.etree.ElementTree as ET
import re
from layout import Ui_MainWindow

# rozmiar jednego heksagonu
hexSize = 60
# Grid ma wymiary (wymiar x wymiar x wymiar)
wymiar = 3

emptyChar = ""
debug = False


# Zamienia stringa na listę list
def convert(string):
    sets = re.findall(r'(?<=\[)[0-9,\,\w\'\s]*?(?=\])', string)
    converted = []
    for set in sets:
        x_coord = int(set[0])
        y_coord = int(set[3])
        value_coord = re.findall(r'(?<=\')[0-9\s]*?(?=\')', set)[0]
        changed = bool(re.findall(r'[a-z|A-Z]+', set)[0])
        converted.append([x_coord, y_coord, value_coord, changed])
    return converted


# Klasa zawierająca kody kolorów do kolorowej konsoli
class Colors:
    BLACK = '\u001b[30m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    BLUE = '\u001b[34m'
    MAGENTA = '\u001b[35m'
    CYAN= '\u001b[36m'
    WHITE = '\u001b[37m'
    ENDC = '\033[0m'


# Klasa do opisująca pojedynczy sześciokąt
class Hexagon(QGraphicsItem):
    def __init__(self, scene, idx, idy, label):
        super().__init__()
        sqrt3 = math.sqrt(3)
        self.x = idx * sqrt3 * hexSize / 2
        self.y = idy * hexSize * 3 / 2

        # Punkty będące wierzchołkami szesciokąta
        self.shape = QPolygonF([
            QPoint(self.x, self.y - hexSize),
            QPoint(self.x + hexSize * sqrt3 / 2, self.y - hexSize / 2),
            QPoint(self.x + hexSize * sqrt3 / 2, self.y + hexSize / 2),
            QPoint(self.x, self.y + hexSize),
            QPoint(self.x - hexSize * sqrt3 / 2, self.y + hexSize / 2),
            QPoint(self.x - hexSize * sqrt3 / 2, self.y - hexSize / 2)], )

        self.scene = scene

        scene.addPolygon(self.shape)
        if debug:
            text = scene.addText(str(idx) + "," + str(idy))
            text.setPos(self.x - text.boundingRect().width() / 2, self.y - text.boundingRect().height() / 2)
        else:
            text = scene.addText(str(label))
            text.setPos(self.x - text.boundingRect().width() / 2, self.y - text.boundingRect().height()/2)



def create_scene(scena, grid):
    scena.clear()
    for pole in grid.pola:
        scena.addPolygon(Hexagon(scena, pole[0], pole[1], pole[2]).shape)


class GridModel:
    def __init__(self, grid_size, scene):
        super().__init__()
        self.pola = []
        self.scene = scene
        middle = grid_size - 1
        start_idx = 0
        end_idx = (grid_size * 2 - 1) * 2

        self.firstx = middle
        self.lastx = middle + middle * 2
        self.lasty = middle * 2
        for i in range(grid_size):
            for j in range(start_idx, end_idx, 2):
                if i > 0:
                    self.pola.append([j, middle - i, "", False])
                self.pola.append([j, middle + i, "", False])
            start_idx += 1
            end_idx -= 1
        self.new_number()

    def new_number(self):
        newx = random.randint(0, len(self.pola)-1)
        occupied = [newx]
        while self.pola[newx][2] != emptyChar:
            newx = random.randint(0, len(self.pola) - 1)
            occupied.append(newx)
            if len(occupied) == len(self.pola):
                return
        self.pola[newx][2] = "2"


    def update_hex_text(self, x, y, new_label, combinedValue = False):
        for pole in self.pola:
            if pole[0] == x and pole[1] == y:
                pole[2] = new_label
                pole[3] = combinedValue
                break

    def get_cell_value(self, x, y):
        for pole in self.pola:
            if pole[0] == x and pole[1] == y:
                return str(pole[2]),pole[3]
        return "0", False

    def save_state(self):
        # root = ET.Element("state")
        # root.text = str(self.pola)
        #
        # mydata = ET.tostring(root)
        # myfile = open("state.xml", "w")
        # myfile.write(str(mydata))
        xml_doc = ET.Element('root')
        product = ET.SubElement(xml_doc, 'saved_state').text = str(self.pola)

        tree = ET.ElementTree(xml_doc)
        tree.write("state.xml", encoding='UTF-8', xml_declaration=True)
        print("\nZAPISANO")


    def load_state(self):
        try:
            with open("state.xml",'rt') as f:
                tree = ET.ElementTree()
                tree.parse(f)
                saved_state = tree.find("saved_state").text
                self.pola = convert(saved_state)
                create_scene(self.scene, self)
            print("\nWCZYTANO")
        except:
            print("Plik z zapisaną grą nie został znaleziony!")



    def move_element(self, startx, starty, endx, endy):
        end_label, endAlreadyCombined = self.get_cell_value(endx, endy)
        start_label, startAlreadyCombined = self.get_cell_value(startx, starty)
        # print(startx, ",", starty, "do ", endx, ",", endy, "labele: ", start_label,end_label)
        if start_label == end_label and start_label != emptyChar and not startAlreadyCombined and not endAlreadyCombined:
            self.update_hex_text(endx, endy, str(int(start_label)+int(end_label)), True)
            self.update_hex_text(startx, starty, emptyChar)
            return True
        elif start_label != emptyChar and end_label == emptyChar:
            self.update_hex_text(endx, endy, start_label, startAlreadyCombined)
            self.update_hex_text(startx, starty, emptyChar)
            return True
        else:
            return False

    def moveW(self):
        retVal = False
        startx = self.firstx
        stopx = self.lastx
        stepx = -1

        for y in range(self.lasty + 1):
            x = startx + 2
            while x <= stopx:
                if self.move_element(x, y, x - 2, y):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
            startx += stepx
            stopx -= stepx
        return retVal

    def moveE(self):
        retVal = False
        startx = self.firstx
        stopx = self.lastx
        stepx = -1
        for y in range(self.lasty + 1):
            x = stopx - 2
            while x >= startx:
                if self.move_element(x, y, x + 2, y) :
                    retVal = True
                x -= 2
            if startx == 0:
                stepx = - stepx
            startx += stepx
            stopx -= stepx
        return retVal

    def moveNE(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        stepx = -1
        offset = -2
        for y in range(1, self.lasty + 1):
            x = startx
            while x <= stopx + offset:
                if debug:
                    print("startx: " + str(startx) + " stepx: " + str(stepx) + "," + str(x) + ":" + str(y))
                if self.move_element(x, y, x + 1, y-1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                offset = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def moveNW(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        stepx = -1
        offsetx = 2
        for y in range(1, self.lasty + 1):
            x = startx + offsetx
            while x <= stopx:
                if debug:
                    print("startx: " + str(startx) + " stepx: " + str(stepx) + "," + str(x) + ":" + str(y))
                if self.move_element(x, y, x - 1, y - 1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                offsetx = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def moveSW(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        stepx = -1
        offsetx = 2
        for y in range(self.lasty - 1, -1, -1):
            x = startx + offsetx
            while x <= stopx:
                if debug:
                    print("startx: "+str(startx)+" stepx: "+str(stepx)+","+str(x)+":"+str(y))
                if self.move_element(x, y, x - 1, y + 1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                offsetx = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def moveSE(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        xoffset = 2
        stepx = -1
        for y in range(self.lasty - 1, -1, -1):
            x = startx
            while x <= stopx - xoffset:
                if debug:
                    print("startx: "+str(startx)+" stepx: "+str(stepx)+","+str(x)+":"+str(y))
                if self.move_element(x, y, x + 1, y + 1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                xoffset = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def clearCombinedFields(self):
        for pole in self.pola:
            pole[3] = False

    def new_game(self):
        for pole in self.pola:
            pole[2] = emptyChar
            pole[3] = False
        print("\nNOWA GRA: ")
        self.new_number()
        create_scene(self.scene, self)

    def moveWFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveW():
            moved = True
            continue
        if moved:
            print(Colors.GREEN + "* lewo (a)" + Colors.ENDC)
            self.new_number()
            create_scene(self.scene, self)



    def moveEFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveE():
            moved = True
            continue
        self.scene.update()
        if moved:
            print(Colors.CYAN + "* prawo (d)" + Colors.ENDC)
            self.new_number()
            create_scene(self.scene, self)

    def moveNEFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveNE():
            moved = True
            continue
        if moved:
            print(Colors.RED + "* góra-prawo (e)" + Colors.ENDC)
            self.new_number()
            create_scene(self.scene, self)



    def moveNWFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveNW():
            moved = True
            continue
        if moved:
            print(Colors.BLUE + "* góra-lewo (q)" + Colors.ENDC)
            self.new_number()
            create_scene(self.scene, self)


    def moveSWFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveSW():
            moved = True
            continue
        if moved:
            print(Colors.MAGENTA + "* dół-lewo (z)" + Colors.ENDC)
            self.new_number()
            create_scene(self.scene, self)

    def moveSEFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveSE():
            moved = True
            continue
        if moved:
            print(Colors.YELLOW + "* dół-prawo (c)" + Colors.ENDC)
            self.new_number()
            create_scene(self.scene, self)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setupUi(self)

        # greenBrush = QBrush(Qt.green)
        # blueBrush = QBrush(Qt.blue)
        # blackPen = QPen(Qt.black)
        # blackPen.setWidth(5)

        self.plansza = GridModel(wymiar, self.scene)

        create_scene(self.scene, self.plansza)

        self.new_game_button.clicked.connect(self.plansza.new_game)
        self.save_button.clicked.connect(self.plansza.save_state)
        self.load_button.clicked.connect(self.plansza.load_state)
        self.NEbutton.clicked.connect(self.plansza.moveNEFull)
        self.Ebutton.clicked.connect(self.plansza.moveEFull)
        self.SEbutton.clicked.connect(self.plansza.moveSEFull)
        self.SWbutton.clicked.connect(self.plansza.moveSWFull)
        self.NWbutton.clicked.connect(self.plansza.moveNWFull)
        self.Wbutton.clicked.connect(self.plansza.moveWFull)
        self.exit_button.clicked.connect(sys.exit)

        # for x in range (rozmiarPlanszy) :
        #     for y in range(rozmiarPlanszy):
        #         hex = Hexagon(scene, x, y, size)
        #         pola.append([hex, x, y])

        self.graphicsView.setScene(self.scene)
        # self.view = QGraphicsView(self.scene, self)
        # self.view.setGeometry(0, 0, 640, 520)
        # self.setWindowTitle("nazwa")
        # self.setGeometry(300, 200, 640, 520)    # (położenie okna x, położenie okna y, szerokość, wysokość)
        self.show()

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

    def mousePressEvent(self, event):
        #super(Window, self).mousePressEvent(event)
        #print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))
        self.tempx = event.x()
        self.tempy = event.y()


    def mouseReleaseEvent(self, event):
        #super(Window, self).mouseReleaseEvent(event)
        delta_y = event.y() - self.tempy
        delta_x = event.x() - self.tempx
        vect_len = math.sqrt(delta_x**2+delta_y**2)
        angle = 180 + math.atan2(delta_y, -delta_x) * 180 / math.pi
        margin = 20
        if vect_len > 100:
            if angle > 360 - margin or angle < 0 + margin:
                self.plansza.moveEFull()
            if 60 - margin < angle < 60 + margin:
                self.plansza.moveNEFull()
            if 120 - margin < angle < 120 + margin:
                self.plansza.moveNWFull()
            if 180 - margin < angle < 180 + margin:
                self.plansza.moveWFull()
            if 240 - margin < angle < 240 + margin:
                self.plansza.moveSWFull()
            if 300 - margin < angle < 300 + margin:
                self.plansza.moveSEFull()





if __name__ == '__main__':
    print("\nSterowanie: q, a, z, e, d, c")
    print("\nHistoria ruchów:")
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
