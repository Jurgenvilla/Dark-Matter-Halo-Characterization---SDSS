#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>

#define N0 50000 //Number of particles

double func(double C, double mu, double sigma){
  return (1.0/(C*sqrt(2.0*M_PI)*sigma))*exp(-((log(C)-mu)*(log(C)-mu))/(2.0*sigma*sigma));
}

int main(void){
  double C; //Random variable
  double mu,sigma,v; //Parameters of the distribution 
  FILE *f; //File to open 
  int i;
  
  //Parameters 
  mu    = 2.9471;
  sigma = 0.33;
  
  f = fopen("concentration.dat","w");
  
  fprintf(f,"#X Y Z\n");
  for(i=1;i<=N0;i++){
    
    do{
      C = drand48()*1e3; //L between 0 and 1e3
      v = drand48()*(0.0670092); //v between 0 and 20.0522 (max of the distribution)
    }
    while (v > func(C,mu,sigma) );
   
    fprintf(f,"%8e\n", C);
  }
  fclose(f);
  
  return 0;
}
    