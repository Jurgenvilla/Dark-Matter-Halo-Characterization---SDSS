import numpy as np
from scipy import integrate

Ell = np.loadtxt("Ell_ZR0.dat",unpack='False')
S0  = np.loadtxt("S0_ZR0.dat",unpack='False')
Sab = np.loadtxt("Sab_ZR0.dat",unpack='False')
Scd = np.loadtxt("Scd_ZR0.dat",unpack='False')

h1 = 0.7
Om = 0.3
Ol = 0.7

N1 = len(Ell[0])
N2 = len(S0[0])
N3 = len(Sab[0])
N4 = len(Scd[0])
  
def H(z):
  return h1*(1.0+z)*np.sqrt(Om*(1.0+z)**3 + Ol)
  
def F(z):
   h = lambda x: (3000.0*1000.0)/(H(x)) #kpc por eso el 1000
   return integrate.quad(h,0.0,z)[0]                                             
 
R0kpc = np.zeros(6)

f = open("Ell_Scale_length.dat","w")

for i in range(N1):
  for k in range(1,6):
    R0kpc[k] = F(Ell[0][i])*( Ell[k][i]*( np.pi/648000.0 ) )
  f.write("%.6e %.6e %.6e %.6e %.6e \n"%(R0kpc[1],R0kpc[2],R0kpc[3],R0kpc[4],R0kpc[5]))
f.close()

f = open("S0_Scale_length.dat","w")

for i in range(N2):
  for k in range(1,6):
    R0kpc[k] = F(S0[0][i])*( S0[k][i]*( np.pi/648000.0 ) )
  f.write("%.6e %.6e %.6e %.6e %.6e \n"%(R0kpc[1],R0kpc[2],R0kpc[3],R0kpc[4],R0kpc[5]))
f.close()

f = open("Sab_Scale_length.dat","w")

for i in range(N3):
  for k in range(1,6):
    R0kpc[k] = F(Sab[0][i])*( Sab[k][i]*( np.pi/648000.0 ) )
  f.write("%.6e %.6e %.6e %.6e %.6e \n"%(R0kpc[1],R0kpc[2],R0kpc[3],R0kpc[4],R0kpc[5]))
f.close()

f = open("Scd_Scale_length.dat","w")

for i in range(N4):
  for k in range(1,6):
    R0kpc[k] = F(Scd[0][i])*( Scd[k][i]*( np.pi/648000.0 ) )
  f.write("%.6e %.6e %.6e %.6e %.6e \n"%(R0kpc[1],R0kpc[2],R0kpc[3],R0kpc[4],R0kpc[5]))
f.close()

