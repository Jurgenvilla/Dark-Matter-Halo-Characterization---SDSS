#======================================================================================================
#Paquetes
#======================================================================================================
import numpy as np
#======================================================================================================
#Archivoss
#======================================================================================================
#Sab
#======================================================================================================

Sab  = np.loadtxt("Data_Table_Sab.dat");print len(Sab)

f = open('ArMstarSab_Mean_STD_VAR.dat','w')
g = open('Sab_selected_galaxies_inbinsdat.dat','w')

Mini=6.5
Mend=11.5
dM=0.3
Niter=int((Mend-Mini)/dM)

print "Binning on", Niter, "mass bins!"



while(Mini<Mend):
  array=[]
  k=0
  for j in range(len(Sab)): # loop sobre las galaxias

    if((Sab[j][0]>=Mini) & (Sab[j][0]<(Mini+dM)) & (Sab[j][2] > 0) & (Sab[j][2] < 2) ):
      g.write("%16.8f %16.8f %16.8f\n"%(Sab[j][0], Sab[j][1], Sab[j][2]))
      aux=Sab[j][1]
      array.append(aux)
      k=k+1
      
  print "Ngals in bin[",Mini,",",Mini+dM,"]=", k  
  mean=np.mean(array)
  median=np.median(array)
  std=np.var(array)
  
  print Mini+dM*0.5,mean,median,std,k
  f.write("%16.8f %16.8f %16.8f %16.8f %12d\n"%(Mini+dM*0.5,mean,median,std,k))

  Mini=Mini+dM

f.close()  
g.close()
#  fin del malparido loop
