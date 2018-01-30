import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

h1  = 0.7
Om = 0.3
Ol = 0.7

q0 = Om/2.0 - Ol

X = np.linspace(0,0.25,100)

def G(z):
  return (4.3e6*z )*(1 + ( (z*(1-q0))/(np.sqrt(1 + 2*q0*z) + 1 + q0*z) ))/(1.0+z)  #Funciona
   
def U(z):
  return (1.83*np.log10(1.0+z)+0.375*np.sin(0.67*z))*(1+z)*4.23e6*(1+z) #kpc   #Funciona 
  
def V(z):
  return z*3e6/0.7 #Extragalactic Astronomy page 156                              #Funciona

def H(z):
  return h1*(1.0+z)*np.sqrt(Om*(1.0+z)**3 + Ol)
  
def F(z):
   h = lambda x: (3000.0*1000.0)/(H(x)) #kpc por eso el 1000
   return integrate.quad(h,0.0,z)[0]                                              #Funciona 

Ythe = []
for z in X:
	Ythe.append( F(z) )

plt.plot(X,V(X), '-', c = 'green', linewidth = 1.5);plt.plot(X,U(X),'-.', c = 'blue',linewidth = 1.5);plt.plot(X,G(X),'--', c = 'red',linewidth = 1.5);plt.plot(X,Ythe,'-', c = 'yellow',linewidth = 1.5)
ax=plt.axes()
ax.legend(['Hubble Law','Mocz-MNRAS', 'DR8-Calibration', 'Our-fit'],loc=4)
ax.set_xlabel("Redshift")                                                  
ax.set_ylabel("D(z) [Kpc]")
plt.grid()
plt.savefig("Functions.png")
plt.show()