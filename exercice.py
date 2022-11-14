#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle

# TODO: Définissez vos fonction ici

def sommeN(N):
    if N < 1:
        return 0
    if N == 1:
        return 2
    if N == 2:
        return 5
    S=5
    n = 3
    nombre_premier = 4
    while n<=N:
        for i in range(2,int(nombre_premier/2)+1):
            if nombre_premier % i == 0:
                break
            elif i == int(nombre_premier/2):
                S+=nombre_premier
                n += 1
            else:
                continue
        nombre_premier+=1
    return S

def ellipsoide(a=2,b=3,c=4,p=10):
    V =(4/3)*math.pi*a*b*c
    return round(V,2),round(V*p,2)

def arbre():
    return None

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    N = 10
    print(f"La somme des {N} premiers nombres entiers premiers est {sommeN(N)}")
    Volume, masse = ellipsoide(5,4,3,10)
    print(f"Le volume de l'ellipsoide est de {Volume} et sa masse est de {masse}.")
    print(f"Le volume de l'ellipsoide initial est de {ellipsoide()[0]} et sa masse est de {ellipsoide()[1]}.")
    turtle.right(15)
