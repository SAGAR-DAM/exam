#Problem 2: decay of radioactive element
#Name: Sagar Dam; Dept: DNAP
from numpy import *
from scipy import integrate
from scipy.optimize import *
from math import *
import matplotlib.pyplot as plt

l=1.5 #in in s**-1

#defining the gradient of time as a function of no of particles
def t(N):
    return -1/(N*l)

N=[]
T=[]
N0=10 #initial particle density in cm**-3
#integrating to get the time as a function of no of particles
for i in range (0,1001):
    T.append(0.01*i)
    y=integrate.romberg(t,N0,N0*exp(-l*0.01*i))
    N.append(N0*exp(-l*y))

#plotting distance from centre vs mass
plt.plot(T,N,'ro',ms=2)
plt.title('time vs no density of particle')
plt.xlabel('time (s)')
plt.ylabel('no density of particle (per cm**3)')
plt.show()