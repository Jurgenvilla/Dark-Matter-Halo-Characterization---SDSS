import numpy as np
import random as random
import matplotlib.pyplot as plt 

S,M = np.loadtxt("SM.dat",unpack='False')

G    = 6.67e-11/(1000.0**3) #Para pasarlos a km**3
Ho   = 2.269e-18 #s-1
md   = 0.05
Dvir = 200.0

f = open("RdCMass.dat","w")
g = open("C.dat","w")

for i in range(500000):
  
  C1    = 10**( (-0.097)*np.log10( 10**M[i]) + ( -110.001/16.885 + 2469.720/(16.885)**2 ) )
  sigma = 0.3
  C     = np.random.normal(C1,sigma)
  
  f_c  = 1.0/np.sqrt( (2.0/3.0) + (C/21.5)**0.7 )
  f_R  = (S[i]/0.1)**(-0.06 + 2.71*md + 0.0047/S[i])*(1 - 3*md + 5.2*md**2)*(1 -0.019*C + 0.00025*C**2 + 0.52/C)
  R = ( (2.0*(10**M[i])*1.98e30*G)/(Dvir*(Ho**2)) )**(1.0/3.0) #sale en km
  
  Rd   = ( ( 1.0/np.sqrt(2) )*S[i]*(R*3.241e-17)*f_c*f_R ) #Sale en kpc 
  
  f.write("%16.8f %16.8f %16.8f\n"%(Rd,C,M[i]))
  g.write("%16.8f \n"%(C))
f.close()  

T,W,Y        = np.loadtxt("RdCMass.dat",unpack='False')
num_bins = 1000.0
Lmax     = np.max(T)
Lmin     = np.min(T)
BINS     = np.linspace(Lmin,Lmax,num_bins)

data = zip(*np.histogram(T,BINS, normed=1))
np.savetxt('RdCMass.txt', data)

plt.hist(T,BINS, normed = 1,fc='g', histtype = 'stepfilled', label = 'Histogram')
plt.xlim(Lmin,8)
plt.xlabel(r'R$_d$ [kpc]')
plt.ylabel('Frequency')
plt.title(r'R$_d$ - Scale Length distribution')
leg = plt.legend()
leg._drawFrame=False

plt.grid()
plt.savefig("Scale_length.png")
plt.show()

  
  
  