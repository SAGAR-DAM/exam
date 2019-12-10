#Problem 5: Mass distribution
#Name: Sagar Dam; Dept: DNAP

from scipy.interpolate import *
import matplotlib.pyplot as plt
import numpy as np

#taking data from given file
fileopen = open("F:\python\data.txt","r")
f = loadtxt("F:\python\data.txt")
theta= f[:,0]
d= f[:,1]
fileopen.close()

#taking input value of theta from user and interpolating d 
t=float(input("Enter the value of theta between (0.1,10):  "))
poly=lagrange(theta,d)  
if (t>=0.01 and t<=10.000000):   
    r=poly(t)
    print("The interpolated value of d at the given value of theta:  ",r)
else:
    print("You haven't given data in the range of interpolation")

#plotting the theoretical interpolation and the data points.
plt.plot(theta,d,'bo',ms=5)
xs = np.linspace(0.1,10.0,1000)
plt.plot(xs, poly(xs), 'r-', lw=3)
plt.title('Lagrange Interpolation for theta and d')
plt.xlabel('theta')
plt.ylabel('d')
plt.show()

#use bisection to find value of theta corresponding to d=370.4
def f(x):
    s=lagrange(theta,d)
    return(s(x))

dexp=370.4
def rootfind(x):
    return f(x)-dexp

root = optimize.bisect(rootfind,0.1,10)
print("The value of theta corresponding to d=370.4 be:  ",root," (using bisection)")