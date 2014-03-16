import multiprocessing
import random
import string
import os
import subprocess

np=5

class Worker(multiprocessing.Process):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.queue=queue

    def run(self):
        print 'Worker started'
        # do some initialization here

        print 'Computing things!'
	
	while True:
          filename = self.queue.get()
          if filename is None:
              break
          #filename=filename[0:filename.rfind("/")+1]+"flow.hpcvel.dat.xtx"
          subprocess.call("./hardyplus 10 10 1 0 1000000 " + filename, shell=True)
          #print "./hardyplus 10 10 1 0 1000000" + filename          
	  #print data 

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def main():
   request_queue = multiprocessing.Queue()
         
   for i in range(np):
     Worker( request_queue ).start()

   #read filenames of lammps executables from metafile
   rootdirpath=os.getcwd()
   with open(rootdirpath+'/metafile.dat','r') as f:
       filenames=f.read().splitlines()

   for line in filenames[0:]:
       line=line[0:line.rfind("/")+1]+"flow.hpcvel.dat.xtx"       
       request_queue.put(line)
   
   #Sentinel objects to allow clean shutdown: 1 per worker.
   for i in range(np):
     request_queue.put( None ) 

main()
