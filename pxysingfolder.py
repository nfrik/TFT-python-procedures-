#Works on files in single folder
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

with open('../python_data/dir1/metadat.txt','r') as f:
       filenames=f.read().splitlines()


tn=0 # - file number
imax=10
jmax=10
fstep=1000 
#filenames=filenames[0:200]
ints=zeros((imax,jmax,shape(filenames)[0]))
for line in filenames[0:1]:
       #frames=range(100000,1001000,1000)
       frames=range(0,size(filenames));
       data=zeros((imax,jmax,shape(frames)[0]));
       t=multiply(frames,0.003*fstep) #timescale 0.003 with frame step (default 1000)        
       print "working on file bin: ", tn, " ", line       
       a = loadtxt(line) #timeframe number
       for i in range(imax):
           for j in range(jmax):
               data[i,j,tn]=a[i][j]
       tn+=1        
#now compute integrals
for i in range(imax):         
   for j in range(jmax):
     ints[i,j]=integrate.simps(data[i,j,:],t)/(max(t)-min(t))
                     
n,bins,patches = P.hist(ints[1,:].reshape(-1).tolist(),normed=1,bins=20,histtype='step',color='green')
#P.setp(patches, 'facecolor','g','alpha',0.75)
x0=mean(ints[1,:].reshape(-1).tolist())
sigma=std(ints[1,:].reshape(-1).tolist())
y=P.normpdf(bins,x0,sigma)
P.plot(bins,y,'k--',linewidth=1.5)
P.show()
