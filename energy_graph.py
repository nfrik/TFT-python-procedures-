import pylab as P
from numpy import *
import numpy

data=numpy.loadtxt('dir1_samp.log')

x=data[0:3300,0]*0.003;
y=data[0:3300,4];

P.plot(x,y,'k-',linewidth=1.5)
P.ylabel(r"Energy, $\epsilon$",size=16)
P.xlabel(r"Time, $\tau$",size=16)
P.show()