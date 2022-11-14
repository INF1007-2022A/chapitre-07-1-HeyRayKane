#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
from turtle import *

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
    begin_fill()
    fd(50)
    end_fill()
    done()

def valide(saisie):
    if len(saisie) == 0:
        return False
    compteur = 0
    for i in saisie:
        if i == "a" or "t" or "g" or "c":
            compteur+=1
    return compteur == len(saisie)

def saisie(type):
    value = input(f"Entrez une {type} valide:\n")

    if valide(value):
        return value

    print(f"La {type} rentrée n'est pas valide.")
    return saisie(type)

def proportion_chaine_ADN(chaine,sequence):
    a=chaine.split(sequence)
    string = str()
    for i in a:
        string+=i
    return chaine,sequence,1 - len(string)/len(chaine)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    N = 10
    print(f"La somme des {N} premiers nombres entiers premiers est {sommeN(N)}")
    Volume, masse = ellipsoide(5,4,3,10)
    print(f"Le volume de l'ellipsoide est de {Volume} et sa masse est de {masse}.")
    print(f"Le volume de l'ellipsoide initial est de {ellipsoide()[0]} et sa masse est de {ellipsoide()[1]}.")
    chaine,sequence,proportion = proportion_chaine_ADN(saisie("chaine"), saisie("sequence"))
    print(f"chaîne : {chaine}\nséquence : {sequence}\nIl y a {round(proportion*100,2)} % de {str(sequence)}.")
