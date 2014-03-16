#Plot atoms positions in scaled frame

import pylab as P
from numpy import *
import numpy
from scipy.ndimage import gaussian_filter1d


f=open('../01262014/ber2nh_02132014/flow.berendsen-nosehoover-wide.dat');
s=f.read();
f.close();
nOfFrames=s.count("ITEM: NUMBER OF ATOMS");
print "number of frames: "+str(nOfFrames)

b=s.splitlines();
nOfAtoms=int(b[3]); #assuming number of atoms doesn't change
nFrame=59; #the frame to display

frameData=[];
for i in range(nOfAtoms):
    frameData.append([float(k) for k in b[(nFrame*(nOfAtoms+9))+9+i].split()]);
    
x=zip(*frameData[:])[1];
y=zip(*frameData[:])[2];
#xy=[[x[i],y[i]] for i in range(size(x))];
#xy.sort(key=lambda tup:tup[1]);

P.figure();
#P.plot(xx,yy,'.');
#P.plot(gaussian_filter1d(xx,150),yy,'r',linewidth=2);
P.plot(x,y,'o');
P.xlabel('Vx');
P.ylabel('y/h');
P.title("Frame: "+str(nFrame)+" NHoover daughter of Berendsen 1200000 steps");
P.show();