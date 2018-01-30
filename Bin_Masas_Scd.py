#======================================================================================================
#Paquetes
#======================================================================================================
import numpy as np
#======================================================================================================
#Archivoss
#======================================================================================================
#Scd
#======================================================================================================

Scd  = np.loadtxt("Data_Table_Scd.dat");print len(Scd) #3 Columns log10 Stellar Mass, R0kpc, n-index Sersic  

f = open('ArMstarScd_Mean_STD_VAR.dat','w')
g = open('Scd_selected_galaxies_inbinsdat.dat','w')

Mini=6.5
Mend=11.5
dM=0.3
Niter=int((Mend-Mini)/dM)

print "Binning on", Niter, "mass bins!"



while(Mini<Mend):
  array=[]
  k=0
  for j in range(len(Scd)): # loop sobre las galaxias

    if((Scd[j][0]>=Mini) & (Scd[j][0]<(Mini+dM)) & (Scd[j][2] > 0) & (Scd[j][2] < 2) ):
      g.write("%16.8f %16.8f %16.8f\n"%(Scd[j][0], Scd[j][1], Scd[j][2]))
      aux=Scd[j][1]
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

