#!/usr/bin/python

import os
import random
import subprocess

rootdirpath=os.getcwd()

with open(rootdirpath+'/metafile.dat','r') as f:
    for line in f:
          line=line[0:line.rfind("/")+1]+"flow.hpcvel.dat.xtx"
          #print line
          subprocess.call("./hardyplus 10 10 1 0 1000000 " + line, shell=True)
f.close()

