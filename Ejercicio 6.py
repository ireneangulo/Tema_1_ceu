# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:27:34 2022

@author: irene
"""
"""
6. Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)
print(impares)
[2, 6]
[1, 5, 7]
Sugerencia
Para ordenar una lista automáticamente puedes utilizar el método .sort().
"""

def par_impar(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    pares.sort()
    impares.sort()
    return pares, impares

lista = [6,5,2,1,7]
par, impar= par_impar(lista)
print('Pares: ', par)
print('Impares: ', impar)
