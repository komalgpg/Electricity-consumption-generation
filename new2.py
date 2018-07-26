# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
from pie_ui import Window1
from pie1_ui import Window2

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

class Ui_Main3(QtGui.QMainWindow):

    def __init__(self):
    	QtGui.QMainWindow.__init__(self)
    	self.setupUi(self)
	self.setWindowState(Qt.WindowMaximized)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1286, 673)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.image3 = QtGui.QLabel(self.centralwidget)
        self.image3.setGeometry(QtCore.QRect(0, 0, 1366, 768))
        self.image3.setText(_fromUtf8(""))
        self.image3.setPixmap(QtGui.QPixmap(_fromUtf8("3.jpg")))
        self.image3.setObjectName(_fromUtf8("image3"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(80, 100, 581, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tlwg Typo"))
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setAutoFillBackground(True)
        self.radioButton.setStyleSheet(_fromUtf8("color rgb(255, 85, 0)\n"
"font: 63 11pt \"Tlwg Typo\";"))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 570, 141, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 210, 581, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tlwg Typo"))
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setAutoFillBackground(True)
        self.radioButton_3.setStyleSheet(_fromUtf8("color rgb(255, 85, 0)\n"
"font: 63 11pt \"Tlwg Typo\";"))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1286, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.radioButton.setText(_translate("MainWindow", "Generation of Electricity in 2016", None))
        self.radioButton.clicked.connect(self.pie1)
        self.pushButton.setText(_translate("MainWindow", "Back", None))
        self.radioButton_3.setText(_translate("MainWindow", "Consumption of Electricity in 2016", None))
        self.radioButton_3.clicked.connect(self.pie2)
	self.pushButton.clicked.connect(self.back1)

    def back1(self):
	self.close()
	
	
    def pie1(self):
    	self.pie1=Window1()
	self.pie1.show()
	
    def pie2(self):
    	self.pie2=Window2()
    	self.pie2.show()
    			

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

