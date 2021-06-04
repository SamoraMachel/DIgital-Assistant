# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyDA.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyDA(object):
    def setupUi(self, PyDA):
        PyDA.setObjectName("PyDA")
        PyDA.resize(647, 42)
        PyDA.setMinimumSize(QtCore.QSize(500, 41))
        PyDA.setMaximumSize(QtCore.QSize(800, 100))
        PyDA.setStyleSheet("QWidget #PyA{\n"
"background-color: rgba(235, 235, 235, 50);\n"
"}\n"
"\n"
"#Query{\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"font-size: 13px\n"
"}\n"
"\n"
"#Speak{\n"
"border: 2px solid #dae4ee;\n"
"border-radius: 10px;\n"
"background-color:  rgb(235, 235, 235);\n"
"}\n"
"\n"
"\n"
"#Query::focus\n"
"{\n"
"border: 2px solid rgb(115,194,251);\n"
"}\n"
"\n"
"#Speak::hover{\n"
"border: 2px solid rgb(115,194,251);\n"
"}")
        self.Query = QtWidgets.QLineEdit(PyDA)
        self.Query.setGeometry(QtCore.QRect(9, 10, 541, 23))
        self.Query.setObjectName("Query")
        self.Speak = QtWidgets.QPushButton(PyDA)
        self.Speak.setGeometry(QtCore.QRect(560, 10, 71, 23))
        self.Speak.setObjectName("Speak")

        self.retranslateUi(PyDA)
        QtCore.QMetaObject.connectSlotsByName(PyDA)

    def retranslateUi(self, PyDA):
        _translate = QtCore.QCoreApplication.translate
        PyDA.setWindowTitle(_translate("PyDA", "PyDA - Digital Assistant"))
        self.Speak.setText(_translate("PyDA", "Speak"))
