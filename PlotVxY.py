import pylab as P
from numpy import *
import numpy
from scipy.ndimage import gaussian_filter1d


f=open('../01262014/ber2nh_02132014/procedural/flow.berendsen-nosehoover-wide.dat');
s=f.read();
f.close();
nOfFrames=s.count("ITEM: NUMBER OF ATOMS");
print "number of frames: "+str(nOfFrames)



b=s.splitlines();
nOfAtoms=int(b[3]); #assuming number of atoms doesn't change
nFrame=600; #the frame to display
nBins=200;#number of bins to display across y axis


frameData=[];
for i in range(nOfAtoms):
    frameData.append([float(k) for k in b[(nFrame*(nOfAtoms+9))+9+i].split()]);
    
x=zip(*frameData[:])[4];
y=zip(*frameData[:])[2];
xy=[[x[i],y[i]] for i in range(size(x))];
xy.sort(key=lambda tup:tup[1]);

xx=[];
yy=[];
atomsPerBin=nOfAtoms/nBins;
##Get averaged along bins
#for i in range(nBins):
#    xx.append(mean([x[0] for x in xy[i*atomsPerBin:(i+1)*atomsPerBin]]));
#    yy.append(mean([y[1] for y in xy[i*atomsPerBin:(i+1)*atomsPerBin]]));
xx=[x[0] for x in xy];
yy=[x[1] for x in xy];

P.figure();
#P.plot(xx,yy,'.');
P.plot(gaussian_filter1d(xx,150),yy,'r',linewidth=2);
P.xlabel('Vx');
P.ylabel('y/h');
P.title("Frame: "+str(nFrame)+" NHoover daughter of Berendsen 1200000 steps");
P.show();