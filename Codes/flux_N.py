#!usr/bin/python3
# coding=utf8

import matplotlib.pyplot as plt
import random
from random import randint
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import mpl,pyplot
from matplotlib import rc

# Paramètres du calcul numérique
npas = 72
dt = 1    
# Paramètres définissant le système physique
N0 = 100       #nombre de voiture totale dans Paris
E0 = 1  #nombre de voiture entrant initiale
O0 = 1  #nombre de voiture sortant initiale

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

def N(t):   #nombre de voitures totales dépendant de flux entrant et sortant
    Nn = []
    Nn.append(N0)
    N = N0
    for t in range(1,npas):
        N = N + entrant_aff[t-1] - sortant_aff[t-1]
        Nn.append(N)
    return Nn

t = np.arange(0, npas)  #intervalle de temps

N_aff = N(t)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t,entrant_aff,"c--", linewidth=1.0,label="flux entrant")
ax.plot(t,sortant_aff,"m--", linewidth=1.0,label="flux sortant")
ax2 = ax.twinx()
ax2.plot(t,N_aff,"g-",linewidth=1.0,label="N")
plt.title("Flux et nombre total de voitures en fonction du temps")
ax.set_xlabel("Temps (h)")
ax.set_ylabel("Amplitude du flux (%)")
ax2.set_ylabel("Nombre total de voitures (ua)")
ax.legend(loc=0)
ax2.legend(loc=0)
plt.show()

