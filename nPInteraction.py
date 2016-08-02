from __future__ import print_function
import numpy as np
import random

def f_ext(x,K):
    #harmonic oscillator's force
    f=-K*x
    return f

def F(a,x):
    #pseudo gravity
    force=0.
    for b in range(len(x)):
        if (a!=b):
            if (abs(x[a]-x[b])>=1):
                force=force+(x[b]-x[a])/(((x[a]-x[b])**2))
    return force

def mv (n):
    fout = open("harout.dat", 'w')

    for a in range(n):
        x[a]=10*random.uniform(-1,1) 
        y[a]=random.uniform(-25, 25)
        vx[a]=random.uniform(-900, 900) 
        vy[a]=random.uniform(-900, 900)
    
    

    for i in range(s):
        for a in range(n):
            #Euler's integrator
            x[a]=vx[a]*dt+x[a]+F(a,x)
            y[a]=vy[a]*dt+y[a]+F(a,y) 
            vx[a]=vx[a]+(f_ext(x[a],K)/m)*dt
            vy[a]=vy[a]+(f_ext(y[a],K)/m)*dt
            
            fout.write("{} {} {} {} {}".format(i, x[a], y[a], vx[a], vy[a]))
        fout.write('\n') 
    fout.close()
    return 

# step number
s=1000
# harmonic oscillator's constant
K=11
# dt= delta t
dt=0.01
# mass 
m=1.

x=np.zeros(n,float)
vx=np.zeros(n,float)
y=np.zeros(n,float)
vy=np.zeros(n,float)  
 
mv(150)