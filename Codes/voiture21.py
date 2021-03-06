#!usr/bin/python3
# coding=utf8

import matplotlib.pyplot as plt
import random
import numpy as np
import math

# Paramètres du calcul numérique
npas = 72
dt = 1    

# Paramètres définissant le système physique
N0 = 100         #nombre de voiture totale dans Paris
c0 = (4/100.) * N0       #nombre de voiture circulant à t=0 


def B(t): 
    if 10.9<np.mod(t, 24)<15:
        B = 10
    else:
        B = 33
    return B


def f(t):
    if 3<np.mod(t, 24)<21:    
        return (B(t) * np.sin((2/8.) * np.pi * t - 4.5) + 37)
    else:
        return 4.


t = np.arange(0, npas+1)
C= np.zeros(npas+1)
C[0]=c0


for i in range(npas):
    C[i+1] = N0 * (f(i)/100)
   
plt.plot(t,C)
plt.title("Nombre de voitures circulant tenant compte des heures de pointe")
plt.xlabel("Temps (h)")
plt.ylabel("Nombre de voitures circulant (ua)")
plt.show()
print(C)


