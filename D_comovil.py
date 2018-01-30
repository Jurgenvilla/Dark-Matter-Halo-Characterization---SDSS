#!/usr/bin/env python
#-*- coding:utf-8 -*-h
#--------------------------------------------------------------------------
#Paquetes
#--------------------------------------------------------------------------
import numpy as np
from scipy import integrate 
#--------------------------------------------------------------------------
#Datos
#--------------------------------------------------------------------------
Ell = np.loadtxt("Ell_ZR0.dat")
S0  = np.loadtxt("S0_ZR0.dat")
Sab = np.loadtxt("Sab_ZR0.dat")
Scd = np.loadtxt("Scd_ZR0.dat")

Z1 = Ell[:,0]
Z2 = S0[:,0]
Z3 = Sab[:,0]
Z4 = Scd[:,0]

A1 = len(Z1)
A2 = len(Z2)
A3 = len(Z3)
A4 = len(Z4)
#--------------------------------------------------------------------------
#Constantes y funciones
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#El resultado dá en parsecs [Mpc]
#--------------------------------------------------------------------------
Om  = 0.3
Ol  = 0.7
h1  = 0.7

def H(z):
  return h1*np.sqrt(Om*(1.+z)**3 + Ol)
  
def f(z):
   h = lambda x: (3000.0)/(H(x))
   return integrate.quad(h,0.0,z)[0]

file = open("DC_Ell.dat","w")
for i in range(A1):
  I = f(Z1[i])
  file.write("%10.4f \n"%I)
file.close()  

file = open("DC_S0.dat","w")
for i in range(A2):
  I = f(Z2[i])
  file.write("%10.4f \n"%I)
file.close()  

file = open("DC_Sab.dat","w")
for i in range(A3):
  I = f(Z3[i])
  file.write("%10.4f \n"%I)
file.close()  

file = open("DC_Scd.dat","w")
for i in range(A4):
  I = f(Z4[i])
  file.write("%10.4f \n"%I)
file.close()  

