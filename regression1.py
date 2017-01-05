import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # for unequal plot boxes
from scipy.optimize import curve_fit
import pandas as pd


import csv

exampleFile = open('darkmatterdensityhalo24redshift133.txt')

exampleFile1 = open('darkmatterradii24redshift133.txt')

exampleReader = csv.reader(exampleFile)
exampleReader1 = csv.reader(exampleFile1)

y1 = list(exampleReader)

r1 = list(exampleReader1)

print len(y1)

print len(r1)



x = 0

y2 = []



while x < len(y1):
	mew = ''.join(y1[x])
	
	y2.insert(x,mew)
	x = x + 1



y3 = map(float,y2)
	



x1 = 0

r2 = []

while x1 < len(r1):
	mew1 = ''.join(r1[x1])
	
	r2.insert(x1,mew1)
	x1 = x1 + 1



y3 = map(float,y2)

r3 = map(float,r2)		


print len(r3)

print len(y3)

print len(r3) - len(y3)
e1 = np.multiply(0.3, y3)



#### NON LINEAR REGRESSION PORTION OF THE PROGRAM



def line(r, a, r0 , n):
	r00 = (r/(r0*1000))**2
	    
	
	return a * r**-n * (1.0 + r/r0)**(-3.0 + n)


param_bounds=([-np.inf,-np.inf,0],[np.inf,np.inf,2])
		
popt, pcov = curve_fit(line, r3, y3, sigma = e1, p0=[10,0.5,1],bounds=param_bounds)

print "a =", popt[0], "+/-", pcov[0,0]**0.5
print "r0 =", popt[1], "+/-", pcov[1,1]**0.5
print "n =", popt[2], "+/-", pcov[2,2]**0.5

axes = plt.gca()
axes.set
plt.errorbar(r3, y3, yerr=e1, fmt= "none")
rfine = np.linspace(0.1, 350., 1500)  # define values to plot the function for
plt.loglog(rfine, line(rfine, popt[0], popt[1],popt[2]), 'r-')
plt.show()



