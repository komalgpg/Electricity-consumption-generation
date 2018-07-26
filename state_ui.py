import sys
from PyQt4 import QtGui,QtCore
import numpy as np
import pandas as pd
import sys
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


class Window4(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Window4, self).__init__(parent)
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
	self.select_button.clicked.connect(self.back4)
	button_layout.addWidget(self.select_button)
	layout.addLayout(button_layout)

	file1 = pd.read_csv('State_gc.csv')
	df=pd.DataFrame(file1)

	cons = list(df.iloc[:31,1])		
	gene = list(df.iloc[:31,2])

	l1 = list(df['State'])
	l2 = ['Consumption','Generation']
	x_pos = np.arange(29)
	
	width = 0.40
	ax = self.figure.add_subplot(111)
	
	# discards the old graph
        ax.clear()
        
	ax.bar(x_pos,cons,width,alpha=0.5,color='r',edgecolor='black',linewidth=0.5,align='center')
        ax.bar([p + width for p in x_pos],
                gene,width,alpha=0.5,color='b',edgecolor='black',linewidth=0.5,align='center')
	ax.set_xticks(x_pos+0.25)
	ax.set_xticklabels(l1,rotation='vertical',fontsize=10)
	ax.set_ylabel('GWH',fontsize=20)
	ax.set_xlabel('States',fontsize=12)
	ax.legend(l2,loc="best",borderpad=2)
	ax.set_title('State-wise Generation & Consumption of Electricity',fontsize=23)
	
	self.canvas.draw()

    def back4(self):
    	self.close()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Window4()
    main.show()
    sys.exit(app.exec_())
    
