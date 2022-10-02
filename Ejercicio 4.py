# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:25:28 2022

@author: irene
"""

"""
Durante la planificación de un proyecto se han acordado una lista 
de tareas. Para cada una de estas tareas se ha asignado un orden de 
prioridad (cuanto menor es el número de orden, más prioridad). ¿Eres 
capaz de crear una estructura del tipo cola con todas las tareas ordenadas 
pero sin los números de orden? Sugerencia Para ordenar automáticamente una 
lista es posible utilizar el método .sort(), deberias probarlo.
"""
from collections import deque

cola= deque(['asearse', 'vueltaacasa', 'universidad', 'deberes', 'almuerzo'])
tareas= ['1 deberes', '2 asearse', '3 almuerzo','4 universidad','5 vueltaacasa' ]
lista_tareas= sorted(tareas, key=len)
print(lista_tareas)
