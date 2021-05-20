
#QRCItem.py > QRCItem > boundingRect

from PySide2 import QtCore
from PySide2.QtWidgets import QGraphicsItem
from PySide2.QtGui import QPixmap, QTransform

import rc_images


class QRCItem(QGraphicsItem):
    def __init__(self, reverse=False):
        super(QRCItem, self).__init__()
        self.reverse = reverse
        self.ItemStacksBehindParent = True
        self.pixmap = QPixmap(":/images/background.png")
        self.pixmap_reflect = self.pixmap.transformed(QTransform().scale(-1, 1))


    def paint_on_screen(self, painter1):
        painter1.setOpacity(0.20)
        if self.reverse:
            painter1.drawPixmap(0, 0, 555, 630, self.pixmap)
        else:
            painter1.drawPixmap(0, 0, 555, 630, self.pixmap_reflect)


    def boundingRect(self):
        return QtCore.QRectf(0, 0, 553, 627)
