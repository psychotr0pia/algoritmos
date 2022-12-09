import math
import numpy as np
import random as rnd
masa = 1
collab = 2
cognitive = 2
maxIter = 1
popSize = 2
valores = [1.5, 2, 3, 1.5, 3, 3, 2]
pesos = [3, 2.5, 3, 2.7, 3, 2.5, 2.6]

def velocidad(velActual, mejorPos, posActual, gBest):
    return(masa*velActual + collab*rnd.random()*(gBest - velActual) + cognitive*rnd.random()*(mejorPos - posActual))

def sigmoide(velocidad):
    return 1/(1 + math.exp(-velocidad))

def posicion(sigmoide):
    r = random()
    if(r < sigmoide):
        return 1
    else:
        return 0
def funcionObjetivo(posicion):
    valor = 0
    for i in range(len(posicion)):
       valor = valor + posicion[i]*valores[i]
    return valor

def pesoTotal(posicion):

    peso = 0
    for i in range(len(posicion)):
        peso = peso + posicion[i]*pesos[i]
    return peso
