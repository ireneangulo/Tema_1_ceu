# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:24:20 2022

@author: irene
"""
"""
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ,01"
"""
cadena = "zeréP nauJ,01"
frase= cadena[::-1].split( ',')
print( frase[1] + " ha sacado un " + frase[0] + " de nota")
