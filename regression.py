import sys
import datetime
from PyQt4 import QtCore,QtGui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

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

list1 = []

class Ui_Form(QtGui.QDialog):
    
    def __init__(self):
    	QtGui.QDialog.__init__(self)
    	self.setupUi(self)		    
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(436, 226)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 41, 431, 181))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 431, 41))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
	today = datetime.datetime.today().strftime('%d/%m/%Y')	
 	self.lineEdit.setText(today)
 	self.lineEdit.setReadOnly(1)
 	self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
    	self.tableWidget.setRowCount(4)
	self.tableWidget.setColumnCount(4)
	self.tableWidget.setHorizontalHeaderLabels(["Months","Units(kWh)","Cost per unit","Total Cost"])
	labels = ['September','October','November','December']

	cost = []
	for i in range(4):
		if(list1[i]<100):
			cost.append(2.96)
		elif(list1[i]>100 and list1[i]<=300):
			cost.append(5.56)
		elif(list1[i]>300 and list1[i]<=500):
			cost.append(9.16)
		else:
		        cost.append(10.61)
	
	total = []
	for i in range(4):
		total.append(round(list1[i]*cost[i],2))
	
	enteries = labels+list1+cost+total
	
	j=k=0
	while(j<4):
		i=0
		while(i<4):
			self.tableWidget.setItem(i,j,QtGui.QTableWidgetItem(str(enteries[k])))
			i+=1
			k+=1
		j+=1	
			
class Window6(QtGui.QDialog):
    
    def __init__(self, parent=None):
        super(Window6, self).__init__(parent)
	self.showMaximized()
       
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
         
	button_layout = QtGui.QHBoxLayout()
	button_layout.addStretch()
	self.push_button = QtGui.QPushButton('View Bill')
	self.push_button.clicked.connect(self.bill)
	button_layout.addWidget(self.push_button)
	layout.addLayout(button_layout)

    
    def start1(self,cno):
	cn = int(cno)

	infile=open('elec.csv',"rb")
	reader=pd.read_csv(infile,sep=',')
	
	df=pd.DataFrame(reader)
	
	li = list(df.iloc[0:10,0])
	
	n = li.index(cn)
	
	l1=list(df.iloc[n,1:9])

	l2=np.array([1,2,3,4,5,6,7,8])
 
 	x=l2
    	y=l1

   
    	b = self.estimate_coef(x, y)
    
    	self.predict(b[0],b[1],l1)
    	
    	
    def estimate_coef(self,x, y):
	
    	# number of observations/points
    	n = np.size(x)
 
    	# mean of x and y vector
    	m_x, m_y = np.mean(x), np.mean(y)
 	
    	# calculating cross-deviation and deviation about x
    	SS_xy = np.sum(y*x - n*m_y*m_x)
    	SS_xx = np.sum(x*x - n*m_x*m_x)
 
    	# calculating regression coefficients
    	b_1 = SS_xy / SS_xx
    	b_0 = m_y - b_1*m_x
 
    	return(b_0, b_1)
 
    	
 
    def predict(self,x1,x2,l1):
	
	for i in range(9,13):
		y = x2*i + x1
		l1.append(round(y,2))
	global list1	
	list1 = l1[8:13]
	
	l3 = [1,2,3,4,5,6,7,8,9,10,11,12]
	points = ['o','o','o','o','o','o','o','o','^','^','^','^']
	color = ['b','b','b','b','b','b','b','b','r','r','r','r']
	
	ax = self.figure.add_subplot(111)

	for xp,yp,m,c in zip(l3,l1,points,color):
		ax.scatter([xp],[yp],marker=m,color=c)
		
	labels1 = [0,'Feb','April','June','Aug','Oct','Dec']	
	ax.set_xticklabels(labels1)	
   	ax.set_xlabel('Months',fontsize=18)
    	ax.set_ylabel('Unit',fontsize=18)

    	self.canvas.draw()

    def bill(self):
    	self.form = Ui_Form()
    	self.form.show()
    
		
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Window = Window6()
    Window6.show()
    sys.exit(app.exec_())		
