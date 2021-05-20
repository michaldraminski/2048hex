# -*- coding: utf-8 -*-

import math

################################################################################
## Form generated from reading UI file 'boardWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QWidget

from GridModel import GridModel
from Hexagon import Hexagon


class Ui_Form(QWidget):

    def __init__(self, wymiar, print_prefix, playerId, callbackObject):
        super().__init__()
        self.wymiar = wymiar
        self.print_prefix = print_prefix
        self.playerId = playerId
        self.enabled = False
        self.callbackObject = callbackObject

    def setupUi(self, Form, x):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10+x, 10, 371+x, 471))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.graphicsView_1 = QGraphicsView(self.frame)
        self.graphicsView_1.setObjectName(u"graphicsView_1")
        self.graphicsView_1.setEnabled(False)
        self.graphicsView_1.setGeometry(QRect(10, 10, 351, 301))
        self.graphicsView_1.setMouseTracking(True)
        self.Ebutton_1 = QPushButton(self.frame)
        self.Ebutton_1.setObjectName(u"Ebutton_1")
        self.Ebutton_1.setGeometry(QRect(200, 370, 50, 40))
        self.NWbutton_1 = QPushButton(self.frame)
        self.NWbutton_1.setObjectName(u"NWbutton_1")
        self.NWbutton_1.setGeometry(QRect(110, 320, 50, 40))
        self.SWbutton_1 = QPushButton(self.frame)
        self.SWbutton_1.setObjectName(u"SWbutton_1")
        self.SWbutton_1.setGeometry(QRect(110, 420, 50, 40))
        self.NEbutton_1 = QPushButton(self.frame)
        self.NEbutton_1.setObjectName(u"NEbutton_1")
        self.NEbutton_1.setGeometry(QRect(170, 320, 50, 40))
        self.Wbutton_1 = QPushButton(self.frame)
        self.Wbutton_1.setObjectName(u"Wbutton_1")
        self.Wbutton_1.setGeometry(QRect(80, 370, 50, 40))
        self.SEbutton_1 = QPushButton(self.frame)
        self.SEbutton_1.setObjectName(u"SEbutton_1")
        self.SEbutton_1.setGeometry(QRect(170, 420, 50, 40))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.scene = QGraphicsScene(self.graphicsView_1)
        self.plansza = GridModel(self.print_prefix, self.wymiar, self.callbackObject)

        self.graphicsView_1.setScene(self.scene)

        self.create_scene()

        self.NEbutton_1.clicked.connect(self.moveNEFull)
        self.Ebutton_1.clicked.connect(self.moveEFull)
        self.SEbutton_1.clicked.connect(self.moveSEFull)
        self.SWbutton_1.clicked.connect(self.moveSWFull)
        self.NWbutton_1.clicked.connect(self.moveNWFull)
        self.Wbutton_1.clicked.connect(self.moveWFull)

        effect = QGraphicsOpacityEffect(self)
        effect.setOpacity(0.8)
        self.graphicsView_1.setGraphicsEffect(effect)
        self.graphicsView_1.setAutoFillBackground(True)
    # setupUi

    def enable(self, enable):
        self.enabled = enable
        self.NEbutton_1.setEnabled(enable)
        self.Ebutton_1.setEnabled(enable)
        self.SEbutton_1.setEnabled(enable)
        self.SWbutton_1.setEnabled(enable)
        self.NWbutton_1.setEnabled(enable)
        self.Wbutton_1.setEnabled(enable)
        self.create_scene()

    def new_game(self, wymiar):
        self.wymiar = wymiar
        self.plansza = GridModel(self.print_prefix, self.wymiar, self.callbackObject)
        #self.callbackObject.print( Colors.RED, "NOWA GRA: ")
        self.plansza.new_number()
        self.create_scene()


    def mouse_pressed(self,x,y):
        if not self.enabled :
            return
        if x < self.frame.x() or x > self.frame.x() +self.frame.width() :
            return
        if y < self.frame.y() or y > self.frame.y() +self.frame.height() :
            return
        self.tempx = x
        self.tempy = y
        #print(self.print_prefix, "tempx", self.tempx)
        #print(self.print_prefix, "tempy", self.tempy)

    def mouse_released(self,x,y):
        if not self.enabled :
            return
        if x < self.frame.x() or x > self.frame.x() +self.frame.width() :
            return
        if y < self.frame.y() or y > self.frame.y() +self.frame.height() :
            return
        delta_y = y - self.tempy
        delta_x = x - self.tempx

        #print(self.print_prefix, "delta_x", delta_x)
        #print(self.print_prefix, "delta_y", delta_y)

        vect_len = math.sqrt(delta_x**2+delta_y**2)
        angle = 180 + math.atan2(delta_y, -delta_x) * 180 / math.pi
        margin = 20
        if vect_len > 40:
            if angle > 360 - margin or angle < 0 + margin:
                self.moveEFull()
            if 60 - margin < angle < 60 + margin:
                self.moveNEFull()
            if 120 - margin < angle < 120 + margin:
                self.moveNWFull()
            if 180 - margin < angle < 180 + margin:
                self.moveWFull()
            if 240 - margin < angle < 240 + margin:
                self.moveSWFull()
            if 300 - margin < angle < 300 + margin:
                self.moveSEFull()
        return

    def moveEFull(self):
        if not self.plansza.moveEFull():
            return
        self.callbackObject.movement(self.playerId, "E")
        self.create_scene()

    def moveNEFull(self):
        if not self.plansza.moveNEFull():
            return
        self.callbackObject.movement(self.playerId, "NE")
        self.create_scene()

    def moveSEFull(self):
        if not self.plansza.moveSEFull():
            return
        self.callbackObject.movement(self.playerId, "SE")
        self.create_scene()

    def moveWFull(self):
        if not self.plansza.moveWFull():
            return
        self.callbackObject.movement(self.playerId, "W")
        self.create_scene()

    def moveNWFull(self):
        if not self.plansza.moveNWFull():
            return
        self.callbackObject.movement(self.playerId, "NW")
        self.create_scene()

    def moveSWFull(self):
        if not self.plansza.moveSWFull():
            return
        self.callbackObject.movement(self.playerId, "SW")
        self.create_scene()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Ebutton_1.setText(QCoreApplication.translate("Form", u"E", None))
        self.NWbutton_1.setText(QCoreApplication.translate("Form", u"NW", None))
        self.SWbutton_1.setText(QCoreApplication.translate("Form", u"SW", None))
        self.NEbutton_1.setText(QCoreApplication.translate("Form", u"NE", None))
        self.Wbutton_1.setText(QCoreApplication.translate("Form", u"W", None))
        self.SEbutton_1.setText(QCoreApplication.translate("Form", u"SE", None))
    # retranslateUi

    def create_scene(self):
        self.scene.clear()
        for pole in self.plansza.pola:
            # greenBrush = QBrush(Qt.green)
            # blueBrush = QBrush(Qt.blue)
            pen = QPen()
            if self.enabled :
                pen.setColor(Qt.black)
            else :
                pen.setColor(Qt.gray)
            pen.setWidth(2)
            self.scene.addPolygon(Hexagon(self.scene, pole[0], pole[1], pole[2],self.enabled, 30/self.wymiar*3).shape,pen)

