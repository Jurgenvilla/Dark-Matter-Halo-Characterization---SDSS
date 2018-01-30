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
S        = np.loadtxt("spin.dat")
num_bins = 224.0
BINS     = np.linspace(0.0007,0.16,num_bins)
X        = np.linspace(0.0007,0.16,1000)
L0       = 0.0307475
sigmaI   = 0.578026
#============================================================
#Histograma
#============================================================
mu       = S.mean()    
sigma    = S.std()   #Calculos estadisticos 
variance = S.var()

print mu,sigma,variance

def f(L):
  return ( 1.0/( L*np.sqrt( 2.0*np.pi)*sigmaI ) )*np.exp(- (np.log( L/L0 ) )**2/( 2.0*sigmaI**2 ) ) #Funcion para el ajuste 

data = zip(*np.histogram(S,BINS, normed = 1))
np.savetxt('Spin_50000.txt', data)                      #Para guardar los datos del histograma y optimizarlos con gnuplot 
#=============================================================
#Graficado
#=============================================================
plt.plot(X, f(X), label = r'f$\lambda$($\lambda$)')
plt.hist(S,BINS, normed = 1, histtype = 'step', label = 'Histogram')
plt.ylim(0,30)
plt.xlim(0.0007,0.16)
plt.xlabel(r'$\lambda$')
plt.ylabel('Frequency')
plt.title(r'f$\lambda$($\lambda$) distribution')
leg = plt.legend()
leg._drawFrame=False

plt.grid()
plt.savefig("Spin.png")
#plt.show()