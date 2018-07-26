import sys
from PyQt4 import QtGui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Window2(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
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
	self.back_button.clicked.connect(self.back2)
	button_layout.addWidget(self.back_button)
	layout.addLayout(button_layout)
	
    	ifile2 = open('ec1.csv',"rb")
	reader = pd.read_csv(ifile2,sep=',')
	
	df = pd.DataFrame(reader)
	
	l1 = df.iloc[70,2:8]
	l2 = ['Domestic','Commercial','Industrial','Traction','Agriculture','Misc']
	cols = ['#191970','#001CF0','#0055D4','#00FF80','#00C69C','#00AAAA']
	
        ax = self.figure.add_subplot(111)
        # discards the old graph
        ax.clear()
       
	ax.pie(l1,colors=cols,shadow=True,autopct='%1.1f%%',startangle=90)
	ax.axis('equal')
	ax.legend(l2,loc="upper right",borderpad=2,title='Major Sectors',fontsize=14)
	ax.set_title('Electricity Consumption by Major Sectors in 2016 \n',fontsize=25)
        
        # refresh canvas"""
        self.canvas.draw()

    def back2(self):
    	self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Window2()
    main.show()

    sys.exit(app.exec_())
    
