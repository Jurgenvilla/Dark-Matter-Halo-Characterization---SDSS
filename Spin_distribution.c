#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

#define N0 50000 //Number of particles

double func(double L, double L0, double sigma){
  return (1.0/(L*sqrt(2.0*M_PI)*sigma))*exp(-((log(L/L0)*log(L/L0))/(2.0*sigma*sigma)));
}

int main(void){
  double L; //Random variable
  double L0,sigma,v; //Parameters of the distribution 
  FILE *f; //File to open 
  int i;
  
  //Parameters 
  L0    = 0.031;
  sigma = 0.57;
  
  f = fopen("spin.dat","w");
  
  fprintf(f,"#X Y Z\n");
  for(i=1;i<=N0;i++){
    
    do{
      L = drand48()*1e3; //L between 0 and 1e3
      v = drand48()*(26.5598); //v between 0 and 20.0522 (max of the distribution)
    }
    while (v > func(L,L0,sigma) );
   
    fprintf(f,"%8e\n", L);
  }
  fclose(f);
  
  return 0;
}
    