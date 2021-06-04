# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Instagram.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import icons_rc

class Ui_instagram(object):
    def setupUi(self, instagram):
        instagram.setObjectName("instagram")
        instagram.resize(256, 162)
        instagram.setMinimumSize(QtCore.QSize(256, 162))
        instagram.setMaximumSize(QtCore.QSize(256, 162))
        instagram.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.529, y1:0.232, x2:0.602273, y2:0.972, stop:0 rgba(185, 0, 117, 255), stop:0.994318 rgba(255, 23, 23, 255));\n"
"}")
        self.label = QtWidgets.QLabel(instagram)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label.setStyleSheet("font-size: 12px;\n"
"color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(instagram)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.label_2.setStyleSheet("font-size: 12px;\n"
"color: white;")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(instagram)
        self.username.setGeometry(QtCore.QRect(90, 20, 133, 23))
        self.username.setStyleSheet("font-size: 12px;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(instagram)
        self.password.setGeometry(QtCore.QRect(90, 60, 133, 23))
        self.password.setStyleSheet("color: green;\n"
"font-size: 12px;\n")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login_2 = QtWidgets.QToolButton(instagram)
        self.login_2.setGeometry(QtCore.QRect(110, 110, 61, 31))
        self.login_2.setStyleSheet("color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0.529727, y1:0.784, x2:0.534591, y2:0.097, stop:0 rgba(0, 147, 255, 255), stop:0.994318 rgba(0, 169, 255, 255));\n"
"font-size: 14px;\n"
"font-family: \"Comis Sans\";\n"
"border-radius: 15px;")
        self.login_2.setIconSize(QtCore.QSize(25, 25))
        self.login_2.setAutoRepeat(False)
        self.login_2.setAutoRepeatInterval(97)
        self.login_2.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.login_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.login_2.setAutoRaise(True)
        self.login_2.setObjectName("login_2")

        self.retranslateUi(instagram)
        self.label.linkActivated['QString'].connect(self.username.setFocus)
        self.label_2.linkActivated['QString'].connect(self.password.setFocus)
        QtCore.QMetaObject.connectSlotsByName(instagram)

    def retranslateUi(self, instagram):
        _translate = QtCore.QCoreApplication.translate
        instagram.setWindowTitle(_translate("instagram", "Authentication"))
        self.label.setText(_translate("instagram", "Username"))
        self.label_2.setText(_translate("instagram", "Password"))
        self.username.setPlaceholderText(_translate("instagram", "pydevjnr"))
        self.password.setPlaceholderText(_translate("instagram", "password"))
        self.login_2.setText(_translate("instagram", "Log In"))
        self.login_2.setShortcut(_translate("instagram", "Ctrl+R"))

