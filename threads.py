
#!/usr/bin/python

import os
import random
import subprocess

import threading
import time

rootdirpath=os.getcwd()

class myThread (threading.Thread):
    def __init__(self,threadID,name,counter,filepath):
	threading.Thread.__init__(self)
	self.threadID = threadID
        self.name = name
        self.counter = counter
        self.path = filepath

    def run(self):
        print "Starting " + self.path
        #print_time(self.name, self.counter, 5)
        analyze_file(self.path)
	print "Finishing " + self.path

def print_time(threadName,delay,counter):
        for i in range(0,counter):
          time.sleep(delay)
          print "%s: %s" % (threadName, time.ctime(time.time()))

def analyze_file(filename):
	#trim and replace filename 
	filename=filename[0:filename.rfind("/")+1]+"flow.hpcvel.dat.xtx"
	#subprocess.call("./hardyplus 10 10 1 0 1000000" + filename, shell=True)
	print "./hardyplus 10 10 1 0 1000000" + filename
	time.sleep(1)	


"""read filenames of lammps executables from metafile"""
with open(rootdirpath+'/metafile.dat','r') as f:
       filenames=f.read().splitlines()

thread1 = myThread(1, "Thread-1",1,filenames[0])
thread2 = myThread(2, "Thread-2",2,filenames[1])

thread1.start()
thread2.start()

print "Exiting Main Thread"

#with open(rootdirpath+'/metafile.dat','r') as f:
#    for line in f:
#          line=line[0:line.rfind("/")+1]+"flow.hpcvel.dat.xtx"
#          subprocess.call("./hardyplus 10 10 1 0 1000000 " + line, shell=True)
#f.close()




