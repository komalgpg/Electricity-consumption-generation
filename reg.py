def start(cno):
	cn = int(cno)
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd

	infile=open('elec.csv',"rb")
	reader=pd.read_csv(infile,sep=',')
	
	df=pd.DataFrame(reader)
	
	li = list(df.iloc[0:10,0])
	
	n = li.index(cn)
	
	l1=df.iloc[n,1:9]
	
	l2=np.array([1,2,3,4,5,6,7,8])

	x=l2
    	y=l1

    	# estimating coefficients
    	b = estimate_coef(x, y)
 
    	# plotting regression line
    	plot_regression_line(x, y, b)

 
def estimate_coef(x, y):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

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
 
def plot_regression_line(x, y, b):

    import matplotlib.pyplot as plt
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    labels = ['Jan','Feb','March','April','May','June','July','Aug']
    plt.xticks(x,labels,rotation='vertical')
    plt.xlabel('Months',fontsize=20)
    plt.ylabel('Units',fontsize=20)
    stringp = 'y = '+str(round(b[1],2))+'x '+str(round(b[0],2))
    plt.text(.35,80.95,stringp,fontsize=18)	
 	
 	
 	
    # function to show plot
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.show()
   
