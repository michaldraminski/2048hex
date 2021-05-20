# Klasa do opisująca pojedynczy sześciokąt

import math
from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PySide2.QtGui import QBrush, QPen, QPolygonF, QKeyEvent, QFont
from PySide2.QtCore import Qt, QPoint


class Hexagon(QGraphicsItem):
    def __init__(self, scene, idx, idy, label, enabled, hexSize):
        super().__init__()
        sqrt3 = math.sqrt(3)
        self.x = idx * sqrt3 * hexSize / 2 + hexSize + 10
        self.y = idy * hexSize * 3 / 2 + hexSize + 10

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
        serifFont = QFont(str(label), 20/30*hexSize, QFont.Bold)
        text = scene.addText(str(label), serifFont)
        if not enabled :
            text.setDefaultTextColor(Qt.gray)
        text.setPos(self.x - text.boundingRect().width() / 2, self.y - text.boundingRect().height()/2)


