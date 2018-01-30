#!/usr/bin/env python
#-*- coding:utf-8 -*-h

import numpy as np

R = np.loadtxt("R01_parsec.dat")
A = np.loadtxt("A1_mag.dat")

r = len(R)
Md = np.zeros(5)

file = open("Md1.dat","w")

for i in range(r):
  for j in range(5):
    Md[j] = 2*np.pi*A[i][j]*(R[i][j])**2
  file.write("%.6e %.6e %.6e %.6e %.6e \n"%(Md[0],Md[1],Md[2],Md[3],Md[4]))
file.close()  