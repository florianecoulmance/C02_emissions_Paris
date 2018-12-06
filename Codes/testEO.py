#!usr/bin/python3
# coding=utf8

import matplotlib.pyplot as plt
import random
from random import randint
import numpy as np
import math

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



t = np.arange(0, npas)  #intervalle de temps


plt.plot (t,entrant_aff,"c-", linewidth=1.0,label="flux entrant")
plt.plot (t,sortant_aff,"m-", linewidth=1.0,label="flux sortant")
plt.title("Allure des flux entrant et sortant (caractere aleatoire)")
plt.xlabel("Temps (h)")
plt.ylabel("Amplitude du flux (%)")
plt.legend()
plt.show()

