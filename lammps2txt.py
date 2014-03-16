#!/usr/bin/python
#COnvert files in /metafile.dat leaving header only for the first frame and adding last column with the number of the frame. 
import os
import random
import subprocess

rootdirpath=os.getcwd()

with open(rootdirpath+'/metafile.dat','r') as f:
    for line in f:
          line=line[0:line.rfind("/")+1]+"flow.hpcvel.dat.txt"
       	  #print line
          subprocess.call("./lammps2txt " + line, shell=True)
f.close()
