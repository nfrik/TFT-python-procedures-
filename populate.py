#!/usr/bin/python

#Populate files in current folder
#str = input("Enter your input:");
#print "Received input:", str


import os
import random
import subprocess

str1="""# 2-d LJ flow simulation

dimension	2
boundary	p s p

log         lammps.log

atom_style	atomic
neighbor	0.3 bin #ex: 0.3 bin=lj, skin=0.3sigma
neigh_modify	delay 1

# create geometry

lattice		hex 0.7
region		box block 0 50 0 30 -0.25 0.25
create_box	3 box
create_atoms	1 box
#read_restart initial_state_250000.dat

mass		1 1.0
mass		2 1.0
mass		3 1.0

# LJ potentials

pair_style	lj/cut 1.12246
pair_coeff	* * 1.0 1.0 1.12246

# define groups

region	     1 block INF INF INF 2.5 INF INF
group	     lower region 1
region	     2 block INF INF 27.5 INF INF INF
group	     upper region 2
group	     boundary union lower upper
group	     flow subtract all boundary

region       feRegion block 0 50 2.5 27.5 -0.25 0.25
group        feGroup region feRegion

set	     group lower type 2
set	     group upper type 3

# initial velocities

compute	mobile flow temp
compute	    1 all stress/atom
#compute     PUT flow temp/profile 1 1 0 xy 2 2 out tensor
#velocity     flow create 1.0 481065 temp PUT

"""



str2="""fix	         1 all nve
##fix		NVT all nvt temp 1.0 1.0 0.02 drag 0.2 tchain 1
fix          2 flow temp/rescale 500 1.0 1.0 0.02 0.05

#Langevin Fix
#fix          2 flow langevin 1.0 1.0 50.0 679483

fix_modify   2 temp mobile
#fix_modify    2 temp PUT

# Couette flow

velocity     lower set 0.0 0.0 0.0
velocity     upper set 2.0 0.0 0.0
fix	         3 boundary setforce 0.0 0.0 0.0
fix	         4 all enforce2d

# Run

timestep	0.003
thermo		100
thermo_modify	temp mobile
#thermo_modify   temp PUT

dump		1 all atom 100 dump.flow.dat

#fix extra all print 100 "Temperature = $temperature" file thermo.txt

#dump		2 all  atom 100 flow.hpc.dat
dump	    3 all custom 1000 flow.hpcvel.dat.txt id xs ys zs vx vy vz x y z mass
#fix         7 flow ave/time 1 1 1000 c_PUT file flow.PUT.txt mode vector

#dump myDump all image 100 dump.*.jpg type type
#dump		1 all image 100 image.*.jpg type type# &
#		zoom 1.6 adiam 1.2
#dump_modify	1 pad 5

run 1000000

#write_restart initial_state_250000.dat
write_restart restart_continue.dat"""


rootdirpath=os.getcwd()
fmeta=open(rootdirpath+'/metafile.dat','wb')

for i in range(1,100):
   newdirpath=rootdirpath + '/dir' + str(i)
   if not os.path.exists(newdirpath):
     os.makedirs(newdirpath)
   filepath=newdirpath + '/in.couetteflow.' + str(i)
   fmeta.write(filepath+"\n")  
   f=open(filepath,'wb')
   strv="velocity     flow create 1.0 " + str(random.randint(100000,999999)) + " temp mobile \n"
   f.write(str1+strv+str2)
   f.close()
   os.chdir(newdirpath);
   subprocess.call("mpirun -np 8 lmp_openmpi < " + filepath, shell=True)   
fmeta.close()
os.chdir(rootdirpath)
