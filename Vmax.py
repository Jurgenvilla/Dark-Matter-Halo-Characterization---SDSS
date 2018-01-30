#!/usr/bin/env python
#-*- coding:utf-8 -*-h

import numpy as np
from scipy import integrate  

Ell = np.loadtxt("ZDcEll.dat"); S0  = np.loadtxt("ZDcS0.dat"); Sab = np.loadtxt("ZDcSab.dat"); Scd = np.loadtxt("ZDcScd.dat")

AEll = np.loadtxt("A1_mag.dat"); AS0 = np.loadtxt("A2_mag.dat"); ASab = np.loadtxt("A3_mag.dat"); AScd = np.loadtxt("A4_mag.dat")

Z1 = Ell[:,0]; Z2 = S0[:,0]; Z3 = Sab[:,0]; Z4 = Scd[:,0]

D1 = Ell[:,1]; D2 = S0[:,1]; D3 = Sab[:,1]; D4 = Scd[:,1]

A1 = AEll[:,2]; A2 = AS0[:,2]; A3 = ASab[:,2]; A4 = AScd[:,2] #Solo A en r

Ol = 0.7; Om = 0.3; h1 = 0.7; Zmin = 0.005

def Vmax(z):
  return h1*(1.0+z)**3*np.sqrt(Om*(1.+z)**3 + Ol)

def f(z):
   h = lambda x: 3000.0/(Vmax(x))
   return integrate.quad(h,Zmin,Zmax)[0]
 
file = open("Vmax_Ell.dat","w")
for i in range(len(Z1)):
  Zmax = ( 1.0 + Z1[i] )*10**( (23.0 - A1[i])/10.0 ) - 1.0
  I = f(Z1[i])*D1[i]*D1[i]
  file.write("%.6e \n"%I)
file.close() 