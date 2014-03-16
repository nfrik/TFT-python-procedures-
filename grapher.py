import pylab as P
from numpy import *
import numpy

ints=numpy.load('avPxyInts.npy')
P.figure(1)

for i in range(10):
 x=ints[9-i,:,:].reshape(-1).tolist()
 #n,bins,patches = P.hist(x,normed=1,bins=40,histtype='step',color='red')
 n,bins=histogram(x,40,normed=True)
 #P.setp(patches, 'facecolor','g','alpha',0.75)
 x0=mean(x)
 sigma=std(x)
 y=P.normpdf(bins,x0,sigma)
 y=y/sum(y)+i*0.05
 P.plot(bins,y,'k--',linewidth=1.5)
 P.annotate(r'$\sigma={0:.2f},$ $x0={1:.2f}$'.format(sigma,x0),xy=(max(x),min(y)+0.01),size=12,rotation=0)
P.ylim([-0.05,0.6])
P.xlim([-0.25,0.15])
 
#P.plot([0],[max(y)],'k-')
P.show()
