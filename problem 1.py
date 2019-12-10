#Problem 1: Mass distribution
#Name: Sagar Dam; Dept: DNAP
from numpy import *
from scipy import integrate
from math import *
import matplotlib.pyplot as plt

p=10 #in kg/m**3

#defining the gradient of mass as a function of distance
def m(t):
    return 4*pi*t**2*p

r=[]
M=[]
#integrating to get the mass in a sphere of particular radius
for i in range (0,1001):
    r.append(0.01*i)
    y=integrate.romberg(m,0,0.01*i)
    M.append(y)

#plotting distance from centre vs mass
plt.plot(r,M,'ro',ms=2)
plt.title('mass vs distance')
plt.xlabel('distance in meter')
plt.ylabel('total mass in the sphere in kg')
plt.show()