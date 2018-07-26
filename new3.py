# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
import reg 
import regression

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

class Ui_Main2(QtGui.QMainWindow):

    def __init__(self):
    	QtGui.QMainWindow.__init__(self)
    	self.setupUi(self)
	self.setWindowState(Qt.WindowMaximized)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1281, 663)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.consumer = QtGui.QPushButton(self.centralwidget)
        self.consumer.setGeometry(QtCore.QRect(580, 210, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.consumer.setFont(font)
        self.consumer.setObjectName(_fromUtf8("consumer"))
        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(580, 340, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setObjectName(_fromUtf8("login"))
        self.pic = QtGui.QLabel(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(-40, -40, 1931, 1241))
        self.pic.setText(_fromUtf8(""))
        self.pic.setPixmap(QtGui.QPixmap(_fromUtf8("7.jpg")))
        self.pic.setObjectName(_fromUtf8("pic"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 90, 781, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tlwg Typo"))
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 556, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(830, 210, 181, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.login_2 = QtGui.QPushButton(self.centralwidget)
        self.login_2.setGeometry(QtCore.QRect(580, 440, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.login_2.setFont(font)
        self.login_2.setObjectName(_fromUtf8("login_2"))
        self.pic.raise_()
        self.login.raise_()
        self.consumer.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.login_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.consumer.setText(_translate("MainWindow", "Consumer No", None))
        self.login.setText(_translate("MainWindow", "View Analysis", None))
        self.login.clicked.connect(self.proceed)
        self.label.setText(_translate("MainWindow", "ELECTRICITY UNIT PREDICTION", None))
        self.pushButton.setText(_translate("MainWindow", "BACK", None))
        self.pushButton.clicked.connect(self.back3)
        self.login_2.setText(_translate("MainWindow", "View Prediction", None))
	self.login_2.clicked.connect(self.view)
	
    def back3(self):
	self.close() 
	
    def proceed(self):
    	cno = self.lineEdit.text()	
	reg.start(cno)

    def view(self):
    	cno = self.lineEdit.text()
    	win1 = regression.Window6()	
	win1.start1(cno)
	
	
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Main2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

