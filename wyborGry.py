# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wyborGry.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_wybor_gry(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(259, 298)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 100, 111, 16))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 140, 124, 112))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pbJedenGracz = QPushButton(self.layoutWidget)
        self.pbJedenGracz.setObjectName(u"pbJedenGracz")

        self.verticalLayout.addWidget(self.pbJedenGracz)

        self.pbDwochGraczy = QPushButton(self.layoutWidget)
        self.pbDwochGraczy.setObjectName(u"pbDwochGraczy")

        self.verticalLayout.addWidget(self.pbDwochGraczy)

        self.pbGraczSiecA = QPushButton(self.layoutWidget)
        self.pbGraczSiecA.setObjectName(u"pbGraczSiecA")

        self.verticalLayout.addWidget(self.pbGraczSiecA)

        self.pbGraczSiecB = QPushButton(self.layoutWidget)
        self.pbGraczSiecB.setObjectName(u"pbGraczSiecB")

        self.verticalLayout.addWidget(self.pbGraczSiecB)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 91, 16))
        self.sbWymiar = QSpinBox(Dialog)
        self.sbWymiar.setObjectName(u"sbWymiar")
        self.sbWymiar.setGeometry(QRect(150, 30, 42, 22))
        self.sbWymiar.setMinimum(2)
        self.sbWymiar.setMaximum(6)
        self.sbWymiar.setValue(3)

        self.retranslateUi(Dialog)

        self.pbJedenGracz.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Wybierz typ gry :", None))
        self.pbJedenGracz.setText(QCoreApplication.translate("Dialog", u"Jeden gracz lokalny", None))
        self.pbDwochGraczy.setText(QCoreApplication.translate("Dialog", u"Dw\u00f3ch graczy lokalnych", None))
        self.pbGraczSiecA.setText(QCoreApplication.translate("Dialog", u"Gracz A sieciowy", None))
        self.pbGraczSiecB.setText(QCoreApplication.translate("Dialog", u"Gracz B sieciowy", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Wybierz typ gry :", None))
    # retranslateUi

