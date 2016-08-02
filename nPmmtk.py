from __future__ import print_function
import numpy as np
import random
from MMTK import *
from MMTK.Trajectory import Trajectory,SnapshotGenerator,TrajectoryOutput
from Library import *
from sys import argv

# Construct system
universe = InfiniteUniverse()

n = 10 # particle number

s = 50000 # step number
K = 2 #Harmonic oscillator force constant
dt = 0.001 # step's length
# particles parameter
x = np.zeros(n,float)
vx = np.zeros(n,float)
y = np.zeros(n,float)
vy = np.zeros(n,float)  
fx = np.zeros(n,float)
fy = np.zeros(n,float)
m = np.zeros(n,float)

#lennard jones parameters
e = 5.    #epsilon
d = 1.    #sigma


fout = open("harout.dat",'w')
Eout = open("E.dat",'w')

#variables's values assignment
for a in range(n):
    x[a] = 2.**(1./6.)*d*a
    y[a] = 2.**(1./6.)*d*a
    vx[a] = 0.001*random.uniform(-1,1) 
    vy[a] = 0.001*random.uniform(-1,1)
#    m[a]=1.*random.uniform(0, 1)
    m[a] = 1.
    universe.addObject(Atom('Ar', position = Vector(x[a],y[a],0.)))

universe.writeToFile('u.pdb')

# Create trajectory
trajectory = Trajectory(universe, "nP.nc", "w", "many particles")

# Create the snapshot generator
snapshot = SnapshotGenerator(universe,
                             actions = [TrajectoryOutput(trajectory,
                                                         ["all"],0,None,1)])
fx,fy = Flj(x,y,0,A,B)

# loop over time steps
for i in range(s):
#   calculate forces
#velocity verlet
    for a in range(n):
        # 1/2 velocity
        vx[a] = vx[a]+.5*((f_ext(x[a],K)+fx[a])/m[a])*dt
        vy[a] = vy[a]+.5*((f_ext(y[a],K)+fy[a])/m[a])*dt
        x[a] = vx[a]*dt+x[a]
        y[a] = vy[a]*dt+y[a]
        
        universe.atomList()[a].setPosition(Vector(x[a],y[a],0.))

    fx,fy = Flj(x,y,0,A,B)
    for a in range(n):    
        vx[a] = vx[a]+.5*((f_ext(x[a],K)+fx[a])/m[a])*dt
        vy[a] = vy[a]+.5*((f_ext(y[a],K)+fy[a])/m[a])*dt
        #coordinates's writing
        fout.write("{} {} {} {} {}".format(i*dt,x[a],y[a],vx[a],vy[a]))

    #calculate energy
    ke,hope,vlj,Et = E(x,y,0,vx,vy,0,K,m,n,Alj,Blj)
    Eout.write("{} {} {} {} {} \n".format(i*dt,ke,hope,vlj,Et))
    snapshot()

    fout.write('\n') 

fout.close()
Eout.close()