# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InstaBot.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Bot(object):
    def __init__(self, Bot):
        Bot.setObjectName("Bot")
        Bot.setWindowModality(QtCore.Qt.NonModal)
        Bot.resize(489, 176)
        Bot.setMinimumSize(QtCore.QSize(489, 176))
        Bot.setMaximumSize(QtCore.QSize(489, 176))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(10)
        Bot.setFont(font)
        Bot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Bot.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:pad, x1:0.529, y1:0.232, x2:0.602273, y2:0.972, stop:0 rgba(185, 0, 117, 255), stop:0.994318 rgba(255, 23, 23, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"}")
        self.label = QtWidgets.QLabel(Bot)
        self.label.setGeometry(QtCore.QRect(250, 90, 62, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Bot)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 37, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Bot)
        self.label_3.setGeometry(QtCore.QRect(9, 90, 48, 16))
        self.label_3.setObjectName("label_3")
        self.maximum = QtWidgets.QLineEdit(Bot)
        self.maximum.setGeometry(QtCore.QRect(320, 90, 141, 20))
        self.maximum.setObjectName("maximum")
        self.likes = QtWidgets.QLineEdit(Bot)
        self.likes.setGeometry(QtCore.QRect(320, 50, 141, 20))
        self.likes.setObjectName("likes")
        self.disallow = QtWidgets.QLineEdit(Bot)
        self.disallow.setGeometry(QtCore.QRect(80, 90, 141, 20))
        self.disallow.setObjectName("disallow")
        self.start = QtWidgets.QPushButton(Bot)
        self.start.setGeometry(QtCore.QRect(220, 130, 75, 28))
        self.start.setStyleSheet("#start{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0.529727, y1:0.784, x2:0.534591, y2:0.097, stop:0 rgba(0, 85, 147, 255), stop:0.994318 rgba(0, 88, 133, 255));\n"
"font-size: 14px;\n"
"font-family: \"Comis Sans\";\n"
"border-radius: 13px;\n"
"}\n"
"\n"
"#start::hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.602, y1:1, x2:0.551, y2:0.0175909, stop:0 rgba(0, 110, 178, 255), stop:0.994318 rgba(0, 255, 223, 255));\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Instagram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start.setIcon(icon)
        self.start.setIconSize(QtCore.QSize(17, 17))
        self.start.setObjectName("start")
        self.wed_driver = QtWidgets.QLineEdit(Bot)
        self.wed_driver.setGeometry(QtCore.QRect(160, 10, 141, 20))
        self.wed_driver.setObjectName("wed_driver")
        self.label_4 = QtWidgets.QLabel(Bot)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Bot)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 54, 16))
        self.label_5.setObjectName("label_5")
        self.browser = QtWidgets.QComboBox(Bot)
        self.browser.setGeometry(QtCore.QRect(80, 50, 141, 22))
        self.browser.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.browser.setMouseTracking(False)
        self.browser.setCurrentText("")
        self.browser.setObjectName("browser")
        self.search = QtWidgets.QPushButton(Bot)
        self.search.setGeometry(QtCore.QRect(310, 9, 60, 23))
        self.search.setStyleSheet("#search{\n"
"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0.529727, y1:0.784, x2:0.534591, y2:0.097, stop:0 rgba(0, 85, 147, 255), stop:0.994318 rgba(0, 88, 133, 255));\n"
"font-size: 13px;\n"
"font-family: \"Comis Sans\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#search::hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.602, y1:1, x2:0.551, y2:0.0175909, stop:0 rgba(0, 110, 178, 255), stop:0.994318 rgba(0, 255, 223, 255));\n"
"}")
        self.search.setIconSize(QtCore.QSize(16, 16))
        self.search.setObjectName("search")

        self.retranslateUi(Bot)
        self.label.linkActivated['QString'].connect(self.maximum.setFocus)
        self.label_3.linkActivated['QString'].connect(self.disallow.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Bot)
        Bot.setTabOrder(self.wed_driver, self.search)
        Bot.setTabOrder(self.search, self.browser)
        Bot.setTabOrder(self.browser, self.likes)
        Bot.setTabOrder(self.likes, self.disallow)
        Bot.setTabOrder(self.disallow, self.maximum)
        Bot.setTabOrder(self.maximum, self.start)

    def retranslateUi(self, Bot):
        _translate = QtCore.QCoreApplication.translate
        Bot.setWindowTitle(_translate("Bot", "Bot"))
        self.label.setText(_translate("Bot", "Maximum"))
        self.label_2.setText(_translate("Bot", "Likes"))
        self.label_3.setText(_translate("Bot", "Disallow"))
        self.maximum.setToolTip(_translate("Bot", "Maximum people to follow"))
        self.maximum.setPlaceholderText(_translate("Bot", "100"))
        self.likes.setToolTip(_translate("Bot", "maximum like to give per person"))
        self.likes.setPlaceholderText(_translate("Bot", "4"))
        self.disallow.setToolTip(_translate("Bot", "prevent the bot to follow people past a certain number of followers"))
        self.disallow.setPlaceholderText(_translate("Bot", "1000"))
        self.start.setText(_translate("Bot", "Start"))
        self.wed_driver.setToolTip(_translate("Bot", "Location of the webdriver used to scrape"))
        self.wed_driver.setPlaceholderText(_translate("Bot", "C:\\\\D.."))
        self.label_4.setText(_translate("Bot", "Web Driver"))
        self.label_5.setText(_translate("Bot", "Browser"))
        self.browser.setToolTip(_translate("Bot", "enter the default Browser"))
        self.search.setText(_translate("Bot", "Search"))
import icons_rc
