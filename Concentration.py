#Acceptance-rejection
#============================================================
#Importacion de librerias
#============================================================
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
#============================================================
#Datos y bins
#============================================================
Co       = np.loadtxt("concentration.dat")
num_bins = 224.0
BINS     = np.linspace(0.0007,60,num_bins)
X        = np.linspace(0.0007,60,1000)
muI      = 2.940350
sigmaI   = 0.330614
#============================================================
#Histograma
#============================================================
mu       = Co.mean()    
sigma    = Co.std()   #Calculos estadisticos 
variance = Co.var()

print mu,sigma,variance

def f(C):
  return ( 1.0/( C*np.sqrt( 2.0*np.pi)*sigmaI ) )*np.exp(- ( (np.log( C ) - muI)**2 )/( 2.0*sigmaI**2 ) ) #Funcion para el ajuste 

data = zip(*np.histogram(Co,BINS, normed = 1))
np.savetxt('Concentration_50000.txt', data)                      #Para guardar los datos del histograma y optimizarlos con gnuplot 
#=============================================================
#Graficado
#=============================================================
plt.plot(X, f(X), label = r'f$_c$(c)')
plt.hist(Co,BINS, normed = 1, histtype = 'step', label = 'Histogram')
plt.ylim(0,0.074)
plt.xlim(0.0007,60)
plt.xlabel('c')
plt.ylabel('Frequency')
plt.title(r'f$_c$(c) distribution')
leg = plt.legend()
leg._drawFrame=False

plt.grid()
plt.savefig("Concentration.png")
#plt.show()