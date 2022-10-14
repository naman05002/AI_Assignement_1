from cProfile import label
import numpy as np
import matplotlib.pyplot as pl
yaxis2 = np.array([45.8,29.6,22.5,17.2,9.4])
yaxis1 = np.array([(43+45+41+40+44+34+41+42+46+43)/10,(23+25+28+23+26+25+23+25+27+23)/10,(20+18+16+18+18+16+23+16+18+17)/10,(8+8+9+9+10+10+8+8+11+12)/10,(8+7+5+10+7+6+7+7+8+7)/10])

xaxis = np.array(['100','200','300','400','500'])
pl.plot(xaxis,yaxis1,'bo-',label='Inital')
pl.plot(xaxis,yaxis2,'ro-',label='Optimized')
# pl.plot(xaxis[1],yaxis[1],'r*')


pl.title('Average Fitness Value (10 Random Graphs) V/S Number of Edges')
pl.xlabel("Number of Edges")
pl.ylabel("Fitness Value")
pl.legend()
pl.show()
# print(yaxis)