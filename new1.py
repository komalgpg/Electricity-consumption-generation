# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
from win import Ui_Main1
from new3 import Ui_Main2

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

class Ui_img(QtGui.QMainWindow):

    def __init__(self):
    	QtGui.QMainWindow.__init__(self)
    	self.setupUi(self)
	self.setWindowState(Qt.WindowMaximized)

    def setupUi(self, img):
        img.setObjectName(_fromUtf8("img"))
        img.resize(1277, 747)
        self.centralwidget = QtGui.QWidget(img)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 11, 19))
        self.label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(".designer/backup/ex/e.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 10, 571, 251))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(255, 0, 0)\n"
"font 63 italic 28pt \"Ubuntu\";\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.mainimage = QtGui.QLabel(self.centralwidget)
        self.mainimage.setGeometry(QtCore.QRect(0, 0, 2560, 1440))
        self.mainimage.setText(_fromUtf8(""))
        self.mainimage.setPixmap(QtGui.QPixmap(_fromUtf8("e.png")))
        self.mainimage.setObjectName(_fromUtf8("mainimage"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(750, 410, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 520, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label.raise_()
        self.mainimage.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        img.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(img)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1277, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        img.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(img)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        img.setStatusBar(self.statusbar)

        self.retranslateUi(img)
        QtCore.QMetaObject.connectSlotsByName(img)

    def retranslateUi(self, img):
        img.setWindowTitle(_translate("img", "MainWindow", None))
        self.label_2.setText(_translate("img", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline; color:#0000ff;\">ELECTRICITY CONSUMPTION </span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline; color:#0000ff;\">AND</span></p><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline; color:#0000ff;\">GENERATION</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("img", "ANALYSIS AND PREDICTION", None))
        self.pushButton_2.setText(_translate("img", "ELECTRICITY PATTERNS", None))
	self.pushButton_2.clicked.connect(self.w)
	self.pushButton_3.clicked.connect(self.bl)


    def w(self):
	self.w=Ui_Main1()
	self.w.show()

    
    def bl(self):
	self.bl=Ui_Main2()
	self.bl.show()
	 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    img = QtGui.QMainWindow()
    ui = Ui_img()
    ui.setupUi(img)
    img.show()
    sys.exit(app.exec_())

