import numpy as np
import random
def har(x=0, y=0,vx=0, vy=0,K=11, m=1, s=200,  dt=0.005):
    fout = open("harout.dat", 'w')

    for i in range(s):

        x=x+vx*dt+(-(K/m)*dt*x)*dt/2
        y=vy*dt+y
#        vx=vx-(K/m)*dt*x-0.001*vx
 #       vy=vy-(K/m)*dt*y-0.001*vx
        vx=vx+(((vx+((K/m)*dt*x))+((K/m)*dt*(x+vx*dt+(-(K/m)*dt*x)*dt/2)))+(vx-(K/m)*dt*x))/2
        vy=vy-(K/m)*dt*y#*y-0.5*vy
        # fout.write("{} {} {} {} {}\n".format(i*dt, x, y, vx, vy))
        fout.write("{} {} {}\n".format(i, x, vx))
    
    fout.close()
    return 

har(5,0,-5,5)
#har(random.uniform(-10, 10), random.uniform(-10, 10),
 random.uniform(-100, 100), random.uniform(-100, 100),random.uniform(-100, 100))
