# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Text.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self, Dialog):
        Dialog.setObjectName("PyDa - Information Sector")
        Dialog.resize(650, 471)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Text = QtWidgets.QTextEdit(Dialog)
        self.Text.setStyleSheet("#Text{\n"
"font-size: 13px;\n"
"border: 1px solid black;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#Text::focus{\n"
"border: 2px  solid rgb(0,191,255);\n"
"}")
        self.Text.setObjectName("Text")
        self.horizontalLayout.addWidget(self.Text)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
