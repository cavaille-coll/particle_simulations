from __future__ import print_function
import numpy as np
import random
from Library import *
#from MMTK import *
#from MMTK.Trajectory import Trajectory, SnapshotGenerator, TrajectoryOutput
#from sys import argv


#Construct system
#universe = InfiniteUniverse()

#particles number
n = 5
# step number
s = 100000
#delta t
dt = 0.001
#particles' properties array 
#psition
x = np.zeros(n,float)
y = np.zeros(n,float)
#velocity
vx = np.zeros(n,float)
vy = np.zeros(n,float)  
xd = np.zeros(n,float) 
m = np.zeros(n,float) 
#circle's radius
r = 10.
#square box half length
L = 20.
#particles's radius
radius = 3
vxp = np.zeros(n,float)
vyp = np.zeros(n,float)
fout = open("Billard.dat", 'w')


for a in range(n):
    # random particles positionning between the circle and the box
    phi = random.uniform(0.,2.*np.pi)
    rad = random.uniform(r,L)
    x[a] = rad*np.cos(phi)
    y[a] = rad*np.sin(phi)
    vx[a] = 10*random.uniform(-1, 1) 
    vy[a] = 10*random.uniform(-1, 1)
    m[a] = 1.
##    universe.addObject(Atom('Ar', position=Vector(x[a],y[a],0.)))

##universe.writeToFile('u.pdb')



## Create trajectory
##trajectory = Trajectory(universe, "Billard.nc", "w", "many particles")


## Create the snapshot generator
##snapshot = SnapshotGenerator(universe,
##                             actions = [TrajectoryOutput(trajectory,
##                                                         ["all"], 0, None, 1)])

    
for i in range(s):
    #periodic kinetic energy sampling
    if i%(s/10) == 0:
            ke = .5*(np.dot(vx,m*vx)+np.dot(vy,m*vy))
            print(ke)
      
    for a in range(n):
        
        # position computation
        x[a] = vx[a]*dt+x[a]
        y[a] = vy[a]*dt+y[a]
        
        # square box rebound
        if x[a] >= L :
            vx[a] = -vx[a]
        if x[a] <= -L :
            vx[a] = -vx[a]   
        if y[a] >= L :
            vy[a] =  -vy[a]
        if y[a] <= -L :
            vy[a] = -vy[a]

##       universe.atomList()[a].setPosition(Vector(x[a],y[a],0.))
        
        for b in range(len(x)):
            if (a != b):
                # particle/particle rebound
                if ((((x[a]-x[b])**2)+((y[a]-y[b])**2))**(1/2)) <= radius:
                     vxt = vx[a]
                     vyt = vy[a]
                     vx[a] = vx[b]*(m[b]/m[a])
                     vy[a] = vy[b]*(m[b]/m[a])
                     vx[b] = vxt*(m[a]/m[b])
                     vy[b] = vyt*(m[a]/m[b])
        
        # curved plane rebound
        # = rebound against tangents
        if np.sqrt(((x[a])**2)+((y[a])**2)) <= r:
            #tangent's angle
            phi = -np.arctan2(x[a],y[a])
            #velocity vector's angle
            nu = -np.arctan2(vx[a],vy[a])
            
            
            # turn tangent to rebound against a vertical "wall"
            vxp[a] = -M(vx[a],vy[a])*np.cos(nu-phi)
            vyp[a] = M(vx[a],vy[a])*np.sin(nu-phi)
            #turn back trajectory: real rebound 
            vx[a] = M(vxp[a],vyp[a])*np.cos(nu)
            vy[a] = M(vxp[a],vyp[a])*np.sin(nu)
            

    
        #file output
        fout.write("{} {} {} {} {}".format(i,x[a],y[a],vx[a],vy[a]))
    fout.write('\n') 
fout.close()