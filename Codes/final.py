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
N0 = 100       #nombre de voiture totale dans Paris
E0 = 1  #nombre de voiture entrant initiale
O0 = 1  #nombre de voiture sortant initiale
c0 = (4/100.) * N0       #nombre de voiture circulant à t=0 

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


for i in range(0,npas-1):
    C[i+1] = N_aff[i] * (f(i)/100)

#affichage flux, N et C
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)

#affichage des flux entrant et sortant
p1=ax1.plot(t,entrant_aff,"c:", linewidth=1.0,label="flux entrant")
p2=ax1.plot(t,sortant_aff,"m:", linewidth=1.0,label="flux sortant")
ax1.set_title('Allure des flux entrant et sortant')
ax1.set_ylabel('Amplitude du flux (%)')
ax1.legend()

#affichage N
ax2.plot(t,N_aff,"g--", linewidth=1.0,label="N")
ax2.set_title('Nombre total de voitures') 
ax2.set_ylabel('Nombre (ua)')
ax2.legend()

#affichage C
ax3.plot(t,C,"r-", linewidth=1.0,label="C")
ax3.set_title('Nombre de voitures circulant')
ax3.set_ylabel('Nombre (ua)')
ax3.legend()

plt.xlabel("Temps (h)")

plt.show()

#Diagramme de phase 2D de voitures qui circulent en fonction du nombre total de voitures
plt.plot(N_aff,C,"y-")
plt.title("Portrait de phase 2D : Nombre de voitures circulant en fonction du nombre total de voitures")
plt.xlabel("Nombre total de voitures (ua)")
plt.ylabel("Nombre de voitures circulant (ua)")
plt.show()

#Diagramme de phase 3D de nombre total de voitures en fonction de flux entrant et flux sortant
fig = plt.figure()
ax = Axes3D(fig)
plt.plot(entrant_aff,sortant_aff,N_aff,"y-")
plt.title("Portrait de phase 3D : Nombre total de voitures en fonction des flux entrant et sortant")
ax.set_xlabel("Flux entrant de voitures (%)")
ax.set_ylabel("Flux sortant de voitures (%)")
ax.set_zlabel("Nombre total de voitures (ua)")
axes = pyplot.gca()
axes.yaxis.set_tick_params(color='red')
axes.xaxis.set_tick_params(color='green')
axes.zaxis.set_tick_params(color='blue')
plt.draw()
plt.show()

