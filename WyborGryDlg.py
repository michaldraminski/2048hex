from wyborGry import Ui_Dialog_wybor_gry
from PySide2.QtWidgets import QDialog


class WyborGryDlg(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_wybor_gry()
        self.typGry = 1
        self.ui.setupUi(self)

        self.ui.pbJedenGracz.clicked.connect(self.jedenGracz)
        self.ui.pbDwochGraczy.clicked.connect(self.dwochGraczy)
        self.ui.pbGraczSiecA.clicked.connect(self.graczSiecA)
        self.ui.pbGraczSiecB.clicked.connect(self.graczSiecB)

    def jedenGracz(self):
        print("A")
        self.typGry = 1
        self.close()
        return

    def dwochGraczy(self):
        print("B")
        self.typGry = 2
        self.close()
        return

    def graczSiecA(self):
        print("C")
        self.typGry = 3
        self.close()
        return

    def graczSiecB(self):
        print("D")
        self.typGry = 4
        self.close()
        return

    def wymiar(self):
        return self.ui.sbWymiar.value()