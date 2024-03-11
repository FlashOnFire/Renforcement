# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 09:39:48 2023

@author: ninot
"""

import matplotlib.pyplot as plt
import numpy as np
import string as str
import math as ma

# A NOTER :
# Vous pouvez tester que le chagement de la précision fonctionne
# changer précision change le nombre de points créés sur le graphique
# Le temps est en seconde, il faut mettre une précision inversement
# proportionelle au temps de simulation

T0 = 255
TL = 0
L = 3
D = 1

TEMP = 100


# si temps < 0.01 pas smooth
def SIM_Smooth(temps):
    if (temps >= 0.01):
        precision = 5 + round(10 * ma.sqrt(1 + 2000 / temps))
        if (temps <= 0.04): precision += round(50 / temps)
    else:
        precision = 8000
    SIMULER_Matriciel(precision, temps)


def SIMULER_Matriciel(precision: int, temps):
    global TEMP, L, D, T0, TL

    # créé la matrice (precision x 1) avec les contraintes à l'origine
    B = creer_contraintes(precision)

    if (temps != 0):
        # créé la matrice qui fait les trucs de calcul
        A = creer_Matrice(precision, temps)
        # créé le tableau avec les valeurs de températures
        temp = creer_tableaux_resultat(A, B)
    else:
        temp = []
        for i in range(precision):
            temp.append(T0)
        temp[precision - 1] = TL
    # créé les valeurs en abscisse du tableau
    B = creer_abscisse(precision)
    # créé le plot avce le graphique
    nom = "Système Thermique"
    affiche_courbe_liste(B, temp, nom)


# créé et affiche un sys instationnaire avec des prec différentes
def SIMULER_INSTA2(precD: int, precT: int, temps):
    global L, D, T0, TL

    # créé les abscice, precD+1 valeures
    X = creer_abscisse(precD + 1)
    # créé les conditions initiales
    Li = creer_Liste2(precD)
    L2 = creer_Liste2(precD)
    # calcul du delta t

    dt = temps / precT
    # initialise le graph
    # plt.plot(X,Li)
    print("dt=")
    print(dt)
    print("dx=")
    print(L / precD)
    print("dt/dx=")
    print(dt * precD / L)

    # itère precT+1 fois l'update de la liste
    for i in range(precT + 1):
        #    Li = source_chaleur(Li, dt, precD)
        Li = update_Liste2(Li, dt, precD)
        L2 = update_Liste3(Li, dt, precD)
    plt.plot(X, L2)
    plt.plot(X, Li)

    print("Tmax =", max(Li))
    # affiche le graph
    plt.title("graph 1D instationnaire")
    plt.xlabel("X")
    plt.ylabel("Temperature")
    plt.show()


# affiche un jeu de donné
def affiche_courbe_liste(x: list, y: list, nom: str):
    plt.plot(x, y)
    plt.title(nom)
    plt.xlabel("X")
    plt.ylabel("Temperature")
    plt.show()


# créé la matrice qui permet de calculer l'état du système à temps total.
# il faut augmenter la précision pour les temps cours
def creer_Matrice(precision: int, TEMP_TOTAL):
    global L, D
    Li = []
    dx = L / precision
    dt = TEMP_TOTAL / precision

    for y in range(0, precision):
        for x in range(0, precision):
            Li.append(0)
            if (x == y + 1) or (x == y - 1):
                # equation stationnaire
                Li[y * precision + x] = D / (dx * dx)
            elif (x == y):
                # equation stationnaire
                Li[y * precision + x] = -2 * D / (dx * dx)
                # equation instationnaire
                Li[y * precision + x] += 1 / dt
            if (x == y + 1):
                Li[y * precision + x] -= 1 / dt

    Li[1] = 0
    Li[0] = 1
    Li[precision * precision - 1] = 1
    Li[precision * precision - 2] = 0
    A = np.array(Li)
    A = A.reshape(precision, precision)
    return A


# créer liste init instationnaire
def creer_Liste2(precD: int):
    global T0, TL, L;

    Li = []

    for i in range(precD + 1):
        x = L * i / precD
        Li.append(4 * x * (3 - x))
    return Li;


# retourne la Liste actualisée sans source
def update_Liste2(Li: list, dt, precD):
    global L, D
    # init liste tampon
    Ltemp = np.array(Li)
    # cacul de 1/(dx**2)
    inv_dx2 = (L / precD) ** (-2)
    # cacul de l'etape d'après de la liste -> en fct precD
    for i in range(1, precD):
        Ltemp[i] += D * dt * (Li[i - 1] - 2 * Li[i] + Li[i + 1]) * inv_dx2
    return Ltemp


# retourne la Liste actualisée avec source
def update_Liste3(Li: list, dt, precD):
    global L, D
    # init liste tampon
    Ltemp = np.array(Li)
    # cacul de 1/(dx**2)
    inv_dx2 = (L / precD) ** (-2)
    # cacul de l'etape d'après de la liste -> en fct precD
    for i in range(1, precD):
        Ltemp[i] += D * dt * (Li[i - 1] - 2 * Li[i] + Li[i + 1]) * inv_dx2
        Ltemp[i] += 0.1 * dt  # c'est la seule diff
    return Ltemp


def source_chaleur(Li: list, dt, precD):
    temp = Li
    for i in range(1, precD):
        temp[i] = Li[i] + 1 * dt
    return temp


# créé le vecteur avec les contraintes aux bornes
# ! c'est dans la matrice de calcul qu'on détermine quelle valeures
# sont prises en compte
# tout nul
def creer_contraintes(precision: int):
    global TL, T0
    B = []
    Li = []
    for i in range(0, precision):
        Li.append(0)
    Li[0] = T0
    Li[precision - 1] = TL
    B = np.array(Li)
    B = B.reshape(precision, 1)
    return B


# créé le tableau avec le résultat
def creer_tableaux_resultat(A: list, B: list):
    global L
    # calc A^(-1)*B
    temp = np.matmul(np.linalg.inv(A), B)
    return temp


# créé les valeurs du tableau en abscisse
def creer_abscisse(precision: int):
    B = []
    for i in range(0, precision):
        B.append((i * L) / (precision - 1))
    return B


SIM_Smooth(1)