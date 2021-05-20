
from graczSieciowyA import Ui_DialogGraczSieciowyA
from PySide2.QtWidgets import *
from tcpServer import TcpServer
import threading


class GraczSieciowyADlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogGraczSieciowyA()
        self.ui.setupUi(self)

