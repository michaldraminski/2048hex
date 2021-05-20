from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import QWidget
import rc_images


class QWidgetBackground(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), QPixmap(":/images/background.png"))
        QWidget.paintEvent(self, event)