# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:24:56 2022

@author: irene
"""
"""
Ej 3
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
"""
lista_mundo = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_luna = ["h",'o','l','a',' ', 'l','u','n','a']

lista_repetidos = []

for letra in lista_mundo:
    if letra in lista_luna and letra not in lista_repetidos:
        lista_repetidos.append(letra)

print(lista_repetidos)
