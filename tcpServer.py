import socket
import threading
from PySide2.QtCore import QObject, Signal, Slot
from PyQt5.QtCore import QObject, pyqtSignal

class TcpServer(QObject):
    trigger = pyqtSignal(str)
    def __init__(self, port, gotServerTcpData):
        super().__init__()
        self.port = port
        self.gotServerTcpDataSignal = gotServerTcpData
        self.trigger.connect(self.handle_trigger)

    def handle_trigger(self, data):
        # Show that the slot has been called.
        print("trigger signal received")
        self.gotServerTcpDataSignal(data)

    def startListen(self):
        x = threading.Thread(target=self.listenThread)
        x.start()

    def listenThread(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', self.port))
        s.listen(1)
        conn, addr = s.accept()
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            #self.gotServerTcpDataSignal.emit("Hello")
            #self.callbackObject.gotTcpServerData(data)
            #conn.sendall(data)
            self.trigger.emit(str(data))
        conn.close()
        s.close()

    def close(self):
        return