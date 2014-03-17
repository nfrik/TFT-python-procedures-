#Supposed to work on files withing several folders
#
#
#

import os
from numpy import *
import numpy
from scipy import integrate
import pylab as P
#import string
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#print integrate.simps(pow(np.arange(0,4.,0.01),2),dx=0.01)

   #read filenames of lammps executables from metafile
rootdirpath=os.getcwd()

#with open('../01262014/ber2nh_02132014/procedural/metafile.dat','r') as f:
#       filenames=f.read().splitlines()

with open('../dir1/metadat.txt','r') as f:
       filenames=f.read().splitlines()

fl=0
imax=10
jmax=10
fstep=1000 
#filenames=filenames[0:200]
ints=zeros((imax,jmax,shape(filenames)[0]))
for line in folders:
       #frames=range(100000,1001000,1000)
       frames=range(0,size(filenames));
       data=zeros((imax,jmax,shape(frames)[0],shape(filenames)[0]))
       t=multiply(frames,0.003*fstep) #timescale 0.003 with frame step (default 1000)        
       tn=0 #fl - file number
       print "working on file bin: ", fl       
       for n in frames:
          #pxyfilename=line[0:line.rfind("/")+1]+"P12_t_"+str(n)+".txt"
          pxyfilename=line;
          a = loadtxt(pxyfilename) #timeframe number
          for i in range(imax):         
            for j in range(jmax): 
              data[i,j,tn,fl]=a[i][j]
          tn+=1 #frame iteration
       #now compute integrals
       for i in range(imax):         
          for j in range(jmax):
            ints[i,j,fl]=integrate.simps(data[i,j,:,fl],t)/(max(t)-min(t))
       fl+=1 #file iteration
                     
n,bins,patches = P.hist(ints[1,:,:].reshape(-1).tolist(),normed=1,bins=20,histtype='step',color='green')
#P.setp(patches, 'facecolor','g','alpha',0.75)
x0=mean(ints[1,1,:].reshape(-1).tolist())
sigma=std(ints[1,1,:].reshape(-1).tolist())
y=P.normpdf(bins,x0,sigma)
P.plot(bins,y,'k--',linewidth=1.5)
P.show()
