# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
from new2 import Ui_Main3
from new4 import Ui_Main4


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main1(QtGui.QMainWindow):

    def __init__(self):
    	QtGui.QMainWindow.__init__(self)
    	self.setupUi(self)
	self.setWindowState(Qt.WindowMaximized)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1026, 654)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.image2 = QtGui.QLabel(self.centralwidget)
        self.image2.setStyleSheet(_fromUtf8("color rgb(85, 0, 0)"))
        self.image2.setText(_fromUtf8(""))
        self.image2.setPixmap(QtGui.QPixmap(_fromUtf8("12.jpg")))
        self.image2.setScaledContents(True)
        self.image2.setObjectName(_fromUtf8("image2"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(60, 170, 411, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.radioButton.setFont(font)
        self.radioButton.setAutoFillBackground(True)
        self.radioButton.setStyleSheet(_fromUtf8("font: 63 italic 20pt \"Ubuntu\";"))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 270, 411, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setAutoFillBackground(True)
        self.radioButton_2.setStyleSheet(_fromUtf8("font: 63 italic 20pt \"Ubuntu\";"))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 576, 151, 31))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.radioButton.setText(_translate("MainWindow", "Present Scenario", None))
        self.radioButton_2.setText(_translate("MainWindow", "Comparative Study", None))
        self.pushButton.setText(_translate("MainWindow", "BACK", None))
	self.pushButton.clicked.connect(self.b1)
	self.radioButton.clicked.connect(self.a)
	self.radioButton_2.clicked.connect(self.a1)

    def b1(self):
	self.close()

    def a(self):
	self.a=Ui_Main3()
	self.a.show()

    def a1(self):
	self.a1=Ui_Main4()
	self.a1.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

