# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from QWidgetBackgroud import QWidgetBackground


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 726)
        MainWindow.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u"2048.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidgetBackground(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.new_game_button = QPushButton(self.centralwidget)
        self.new_game_button.setObjectName(u"new_game_button")
        self.new_game_button.setGeometry(QRect(10, 510, 131, 41))
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(150, 510, 131, 41))
        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setGeometry(QRect(290, 510, 121, 41))
        self.undo_button = QPushButton(self.centralwidget)
        self.undo_button.setObjectName(u"undo_button")
        self.undo_button.setGeometry(QRect(420, 510, 71, 41))
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(660, 510, 71, 41))
        self.teLog = QTextEdit(self.centralwidget)
        self.teLog.setObjectName(u"teLog")
        self.teLog.setGeometry(QRect(10, 560, 811, 141))
        self.autoplay_button = QPushButton(self.centralwidget)
        self.autoplay_button.setObjectName(u"autoplay_button")
        self.autoplay_button.setGeometry(QRect(580, 510, 71, 41))
        self.btReplay = QPushButton(self.centralwidget)
        self.btReplay.setObjectName(u"btReplay")
        self.btReplay.setGeometry(QRect(500, 510, 71, 41))
        self.lbStepInfo = QLabel(self.centralwidget)
        self.lbStepInfo.setObjectName(u"lbStepInfo")
        self.lbStepInfo.setGeometry(QRect(750, 520, 47, 13))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 21))
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
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save progress", None))
        self.load_button.setText(QCoreApplication.translate("MainWindow", u"Load saved file", None))
        self.undo_button.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.autoplay_button.setText(QCoreApplication.translate("MainWindow", u"Autoplay", None))
        self.btReplay.setText(QCoreApplication.translate("MainWindow", u"Replay", None))
        self.lbStepInfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

