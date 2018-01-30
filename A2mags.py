#!/usr/bin/env python
#-*- coding:utf-8 -*-h

import numpy as np

A1 = np.loadtxt("A1.dat")
A2 = np.loadtxt("A2.dat")
A3 = np.loadtxt("A3.dat")
A4 = np.loadtxt("A4.dat")

a1 = len(A1)
a2 = len(A2)
a3 = len(A3)
a4 = len(A4)

Amag = np.zeros(5)

file = open("A1_mag.dat","w")

for i in range(a1):
  for j in range(5):
    Amag[j] = 22.5 - 2.5*np.log10(A1[i][j]) 
  file.write("%.6e %.6e %.6e %.6e %.6e \n"%(Amag[0],Amag[1],Amag[2],Amag[3],Amag[4]))
file.close()    

file = open("A2_mag.dat","w")

for i in range(a2):
  for j in range(5):
    Amag[j] = 22.5 - 2.5*np.log10(A2[i][j]) 
  file.write("%.6e %.6e %.6e %.6e %.6e \n"%(Amag[0],Amag[1],Amag[2],Amag[3],Amag[4]))
file.close()  

file = open("A3_mag.dat","w")

for i in range(a3):
  for j in range(5):
    Amag[j] = 22.5 - 2.5*np.log10(A3[i][j]) 
  file.write("%.6e %.6e %.6e %.6e %.6e \n"%(Amag[0],Amag[1],Amag[2],Amag[3],Amag[4]))
file.close()  

file = open("A4_mag.dat","w")

for i in range(a4):
  for j in range(5):
    Amag[j] = 22.5 - 2.5*np.log10(A4[i][j]) 
  file.write("%.6e %.6e %.6e %.6e %.6e \n"%(Amag[0],Amag[1],Amag[2],Amag[3],Amag[4]))
file.close()  