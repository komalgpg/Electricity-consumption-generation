import sys
from PyQt4 import QtGui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Window1(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window1, self).__init__(parent)
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
	self.back_button = QtGui.QPushButton('Back')
	self.back_button.clicked.connect(self.back1)
	button_layout.addWidget(self.back_button)
	layout.addLayout(button_layout)
	
	
    	ifile1 = open('eg1.csv',"rb")
	reader = pd.read_csv(ifile1,sep=',')
	
	df = pd.DataFrame(reader)
	
	l1 = df.iloc[16,1:6]
	l2 = ['Steam','Diesel','Gas','Hydro','ORS']
	cols = ['yellowgreen','lightskyblue','magenta','black','yellow']
	percent = 100.*l1/l1.sum()
	
        ax = self.figure.add_subplot(111)
        ax.clear()
        
        patches,texts = ax.pie(l1,colors=cols,shadow=True,startangle=90,radius=1)
	labels = ['{0}-{1:1.2f}%'.format(i,j) for i,j in zip(l2,percent)]
	
	sort_legend = True
	if sort_legend:
		patches,labels,dummy=zip(*sorted(zip(patches,labels,l1),key=lambda l2:l2[2],reverse=True))
	
	ax.legend(patches,labels,loc="upper right",borderpad=2,title='Generating Sources',fontsize=14,bbox_to_anchor=(1.1,1.))	
	ax.axis('equal')
	ax.set_title('Major Electricity Generating Sources in 2016 \n',fontsize=25)
        
        # refresh canvas"""
        self.canvas.draw()

    def back1(self):
    	self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Window1()
    main.show()

    sys.exit(app.exec_())
    
