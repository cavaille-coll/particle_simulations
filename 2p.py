import numpy as np
import random

def f_ext(x,K):
    #harmonic oscillator's force
    f=-K*x
    return f

def F(a, b):
    #pseudo gravity
    F=(b-a)/(((a-b)**2)+1)
    return F
 
def har(x1=0, y1=0,vx1=0, vy1=0,x2=0, y2=0,vx2=0, vy2=0, x3=5, 
    y3=2, vx3=0, vy3=9, K=11, m1=1, m2=300, m3=1, s=5000, dt=0.01):
   # v(x,y,z) = velocity
   # K = harmonic oscillator's constant
   # m = mass 
   # s = step number
   # dt= delta t
    fout = open("harout.dat", 'w')

    for i in range(s):
        #particle's position computation
        # with Euler's integrator
        x1=vx1*dt+x1+F(x1, x2)+F(x1, x3)
        y1=vy1*dt+y1+F(y1, y2)+F(y1, y3)  
        vx1=vx1+(f_ext(x1,K)/m1)*dt
        vy1=vy1+(f_ext(y1,K)/m1)*dt
        
        x2=vx2*dt+x2+F(x2, x1)+F(x2, x3)
        y2=vy2*dt+y2+F(y2, y1)+F(y2, y3)     
        vx2=vx2+(f_ext(x2,K)/m2)*dt
        vy2=vy2+(f_ext(y2,K)/m2)*dt
        
        x3=vx3*dt+x3+F(x3, x1)*F(x3, x2)
        y3=vy3*dt+y3+F(y3, y1)+F(y3, y2)     
        vx3=vx3+(f_ext(x3,K)/m2)*dt
        vy3=vy3+(f_ext(y3,K)/m2)*dt

        fout.write("{} {} {} {} {}\n".format(i, x1, x2, y1, y2))
    fout.close()
    return 

har(30, 1, 5000, 1, 0, 5, 30, -5)