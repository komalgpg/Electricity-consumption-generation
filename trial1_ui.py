import sys
from PyQt4 import QtGui,QtCore
import numpy as np
import pandas as pd
import sys

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
        
class Window(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
	self.showMaximized()
        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        
        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
	self.setLayout(layout)


	button_layout = QtGui.QHBoxLayout()
	button_layout.addStretch()
	self.select_button = QtGui.QPushButton('Back')
	self.select_button.setFixedWidth(135)
	self.select_button.clicked.connect(self.back3)
	button_layout.addWidget(self.select_button)
	layout.addLayout(button_layout)
    
    	ifile = open('ec1.csv',"rb")
	reader = pd.read_csv(ifile,sep=',')
	df = pd.DataFrame(reader)
	
	ifile3 = open('eg1.csv',"rb")
	reader = pd.read_csv(ifile3,sep=',')
	df1 = pd.DataFrame(reader)
	
	l1 = list(df.iloc[54:71,1])
	l2 = list(df1['Year'])
	x_pos = np.arange(len(l2))
	l3 = list(df1['Grand total'])
	l4 = l1 + l3
	myarray = np.array(l4).reshape(2,17)
	l5 = ['Consumption','Generation']
	width = 0.40
	
        ax = self.figure.add_subplot(111)
	
	# discards the old graph
        ax.clear()
        
	ax.bar(x_pos,myarray[0],width,alpha=0.5,color='r',edgecolor='black',linewidth=0.5,align='center')
        ax.bar([p + width for p in x_pos],
                myarray[1],width,alpha=0.5,color='b',edgecolor='black',linewidth=0.5,align='center')
	ax.set_xticks(x_pos+0.24)
	ax.set_xticklabels(l2,rotation='vertical',fontsize=13)
	ax.set_ylabel('Total Generation (GWh)',fontsize=23)
	ax.set_xlabel('Years',fontsize=19)
	ax.legend(l5,loc="best",borderpad=2)
	ax.set_title('Electricity Growth pattern',fontsize=23)
	
        # refresh canvas"""
        self.canvas.draw()

    def back3(self):
    	self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Window()
    main.show()

    sys.exit(app.exec_())
    
