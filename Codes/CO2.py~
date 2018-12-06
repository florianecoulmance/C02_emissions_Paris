#!usr/bin/python3
# coding=utf8

import matplotlib.pyplot as plt
import random
from random import randint
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import mpl,pyplot

# Paramètres du calcul numérique
npas = 72
dt = 1  
  
# Paramètres définissant le système physique
N0 = 660000       #nombre de voiture totale dans Paris
E0 = 1  #nombre de voiture entrant initiale
O0 = 1  #nombre de voiture sortant initiale
c0 = (4/100.) * N0       #nombre de voiture circulant à t=0 
CO20= 370.      #taux de CO2 dans un environnement non pollué en ppm


#Les flux
E=[]
O=[]
t=[]

def A(t):   #amplitude de la fonction E
    if 4<np.mod(t, 24)<12:
        A = random.randint(30,70)
    else:
        A = 70
    return A

def a(t):   #amplitude de la fonction O
    if 15<np.mod(t, 24)<23:
        a = random.randint(30,70)
    else:
        a = 70
    return a

def entrant():  #flux entrant
    E = []
    time = range(0,npas/3) + range(0,npas/3) + range(0,npas/3)  #répéter la fonction E sur 72 h soit 3 jours
    for t in time:
        E.append(A(t) * np.exp(-((t - 8.)**2)/8))
    return E

entrant_aff = entrant()

def sortant():  #flux sortant
    O = []
    time = range(0,npas/3) + range(0,npas/3) + range(0,npas/3)  #répéter la fonction O sur 72h soit 3 jours
    for t in time:
        O.append(a(t)* np.exp(-((t - 19.)**2)/8))
    return O

sortant_aff = sortant()

#nombre de voitures totales dépendant de flux entrant et sortant
def N(t):   
    Nn = []
    Nn.append(N0)
    N = N0
    for t in range(1,npas):
        N = N + entrant_aff[t-1] - sortant_aff[t-1]
        Nn.append(N)
    return Nn

#definition de la fonction f déterminant beta 
def B(t): #amplitude de f
    if 10.9<np.mod(t, 24)<15:
        B = 10
    else:
        B = 33
    return B


def f(t):   #f déterminant beta
    if 3<np.mod(t, 24)<21:    
        return (B(t) * np.sin((2/8.) * np.pi * t - 4.5) + 37)
    else:
        return 4.

t = np.arange(0, npas)  #intervalle de temps

# on appelle la fonction N nombre de voiture totale après que t soit défini
N_aff = N(t)

C= np.zeros(npas)
C[0]=c0
CO2=np.zeros(npas)
CO2[0]=CO20

for i in range(0,npas-1):
    C[i+1] = N_aff[i] * (f(i)/100)
    CO2[i+1] = N_aff[i] * (f(i)/100) * (0.072*N_aff[i] + 0.048*N_aff[i] + 0.006*N_aff[i])


#affichage C et CO2 en fonction du temps
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,C,"r--", linewidth=1.0,label="C")
ax2 = ax.twinx()
ax2.plot(t,CO2,"g-", linewidth=1.0,label="CO2")
plt.title("Nombre de voitures qui circulent et taux de CO2 en fonction du temps")
ax.set_xlabel("Temps (h)")
ax.set_ylabel("Nombre de voitures (ua)")
ax2.set_ylabel("Taux (ppm)")
ax.legend(loc=0)
ax2.legend(loc=0)
plt.show()



#Portrait de phase 2D du taux de CO2 en fonction du nombre de voitures qui circulent
plt.plot(C,CO2,"m-")
plt.title("Portrait de phase 2D : Taux de CO2 en fonction du nombre de voitures circulant")
plt.xlabel("Nombre de voitures (ua)")
plt.ylabel("Taux (ppm)")
plt.show()

#Portrait de phase 3D du taux de CO2 en fonction du nombre de voitures total et circulant
fig = plt.figure()
ax = Axes3D(fig)
plt.plot(N_aff,C,CO2,"m-")
plt.title("Portrait de phase 3D : Taux de CO2 en fonction du nombre total de voitures et du nombre de voitures circulant")
ax.set_xlabel("Nombre de voitures total (ua)")
ax.set_ylabel("Nombre de voiture circulant (ua)")
ax.set_zlabel("Taux de CO2 (ppm)")
axes = pyplot.gca()
axes.yaxis.set_tick_params(color='red')
axes.xaxis.set_tick_params(color='green')
axes.zaxis.set_tick_params(color='blue')

plt.show()

#Portrait de phase 3D du taux de CO2 en fonction des flux entrant et sortant
fig = plt.figure()
ax = Axes3D(fig)
plt.plot(entrant_aff,sortant_aff,CO2,"c-")
plt.title("Portrait de phase 3D : Taux de CO2 en fonction des flux entrant et sortant")
ax.set_xlabel("Amplitude du flux entrant (%)")
ax.set_ylabel("Amplitude du flux sortant (%)")
ax.set_zlabel("Taux de CO2 (ppm)")
axes = pyplot.gca()
axes.yaxis.set_tick_params(color='red')
axes.xaxis.set_tick_params(color='green')
axes.zaxis.set_tick_params(color='blue')

plt.show()

