import numpy as np
import matplotlib.pyplot as pl
yaxis = np.array([(43+45+41+40+44+34+41+42+46+43)/10,(23+25+28+23+26+25+23+25+27+23)/10,(20+18+16+18+18+16+23+16+18+17)/10,(8+8+9+9+10+10+8+8+11+12)/10,(8+7+5+10+7+6+7+7+8+7)/10])
xaxis = np.array(['100','200','300','400','500'])
pl.plot(xaxis,yaxis,'bo-')
# pl.plot(xaxis[1],yaxis[1],'r*')


pl.title('Average Fitness Value v/s Number of Edges')
pl.xlabel("Number of Edges")
pl.ylabel("Fitness Value")
pl.show()
# print(xaxis)