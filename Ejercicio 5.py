# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 12:42:07 2022

@author: irene
"""
"""
Ejercicio 5
Crea un script llamado descomposicion.py que realice las siguientes tareas:
Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:
python descomposicion.py 3647
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
0007
0040
0600
3000
Pista
Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
"""
def descomponernumero(numero):
    digitos= [int(x) for x in str(numero)]
    for i in range(len(digitos)):
        cifras= digitos[-1-i]*10**i
        cifras= '{:04d}'.format(cifras)
    return (cifras)


def meterunnumero():
    usuario= int(input('Mete un numero: '))
    print(descomponernumero(usuario))
    return(usuario)
    
meterunnumero()

