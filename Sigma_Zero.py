import numpy as np
import matplotlib.pyplot as plt 

#================================================================================================================
#Cosntantes

S01 = 260.365
z   = 0.0
ol  = 0.7
om  = 0.2
Ho  = 70.0
H0z = Ho*np.sqrt(ol + om*(1+z)**3)

G    = 6.67e-11/(1000.0**3) #Para pasarlos a km**3
#M[i] debe ir de la forma [Mi]*1.98e30 para que de en kg 
#Asi el V vir se calcula en km/s

md   = 0.05
#================================================================================================================

S,M,Rd = np.loadtxt("SMRd.dat",unpack='False')

f = open("Sigma_Zero.dat","w")

for i in range(50000):
  
  C    = 10**( (-0.097)*np.log10( 10**M[i]) + ( -110.001/16.885 + 2469.720/(16.885)**2 ) )
  f_c  = (2.0/3.0) + (C/21.5)**0.7 
  f_R  = ((S[i]/0.1)**(-0.06 + 2.71*md + 0.0047/S[i])) * (1.0 - 3.0*md + 5.2*(md**2)) * (1.0 -0.019*C + 0.00025*C**2 + 0.52/C)

  Vvir = 2.15443*(G*(10**M[i])*1.98e30*2.269e-18)**(1.0/3.0)

  S0 = S01*((0.05/S[i])**(2.0))*(Vvir/250.0)*(H0z/Ho)*f_c/(f_R**(2.0))
  
  #El resultado entonces esta en Msol/pc2
  
  f.write("%16.8f \n"%S0)  
f.close()  
#================================================================================================================

T1       = np.loadtxt("Sigma_Zero.dat")
T        = np.log10(T1)
num_bins = 224.0
Lmax     = np.max(T)
Lmin     = np.min(T)
BINS     = np.linspace(Lmin,Lmax,num_bins)

data = zip(*np.histogram(T,BINS, normed=1))
np.savetxt('Sigma_Zero.txt', data)

plt.hist(T,BINS, normed = 1, fc ='darkred',histtype = 'stepfilled', label = 'Histogram')
plt.xlim(Lmin,Lmax)
plt.ylim(0,0.6)
plt.xlabel(r'log ($\Sigma_0$ [M$\odot$ pc$^{-2}$])')
plt.ylabel('Frequency')
plt.title(r'$\Sigma_0$ - Surface density profile')
leg = plt.legend()
leg._drawFrame=False

plt.grid()
plt.savefig("Sigma_Zero.png")
plt.show()

  
  
  