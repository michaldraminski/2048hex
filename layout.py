# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(625, 775)
        MainWindow.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u"2048.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(False)
        self.graphicsView.setGeometry(QRect(0, 0, 621, 571))
        self.graphicsView.setMouseTracking(True)
        self.new_game_button = QPushButton(self.centralwidget)
        self.new_game_button.setObjectName(u"new_game_button")
        self.new_game_button.setGeometry(QRect(400, 580, 131, 41))
        self.NWbutton = QPushButton(self.centralwidget)
        self.NWbutton.setObjectName(u"NWbutton")
        self.NWbutton.setGeometry(QRect(50, 590, 50, 40))
        self.Wbutton = QPushButton(self.centralwidget)
        self.Wbutton.setObjectName(u"Wbutton")
        self.Wbutton.setGeometry(QRect(20, 640, 50, 40))
        self.NEbutton = QPushButton(self.centralwidget)
        self.NEbutton.setObjectName(u"NEbutton")
        self.NEbutton.setGeometry(QRect(110, 590, 50, 40))
        self.SEbutton = QPushButton(self.centralwidget)
        self.SEbutton.setObjectName(u"SEbutton")
        self.SEbutton.setGeometry(QRect(110, 690, 50, 40))
        self.SWbutton = QPushButton(self.centralwidget)
        self.SWbutton.setObjectName(u"SWbutton")
        self.SWbutton.setGeometry(QRect(50, 690, 50, 40))
        self.Ebutton = QPushButton(self.centralwidget)
        self.Ebutton.setObjectName(u"Ebutton")
        self.Ebutton.setGeometry(QRect(140, 640, 50, 40))
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(400, 630, 131, 41))
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(400, 680, 131, 41))
        self.undo_button = QPushButton(self.centralwidget)
        self.undo_button.setObjectName(u"undo_button")
        self.undo_button.setGeometry(QRect(540, 600, 71, 41))
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(540, 650, 71, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 625, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hex2048", None))
        self.new_game_button.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.NWbutton.setText(QCoreApplication.translate("MainWindow", u"NW", None))
        self.Wbutton.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.NEbutton.setText(QCoreApplication.translate("MainWindow", u"NE", None))
        self.SEbutton.setText(QCoreApplication.translate("MainWindow", u"SE", None))
        self.SWbutton.setText(QCoreApplication.translate("MainWindow", u"SW", None))
        self.Ebutton.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save progress", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load saved file", None))
        self.undo_button.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
    # retranslateUi

