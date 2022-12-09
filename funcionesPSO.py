import math
import numpy as np
import random as rnd
masa = 1
collab = 2
cognitive = 2
maxIter = 1
popSize = 2
valores = [2,5,6,10,13,16]
pesos = [1,2,4,5,7,8]

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
    for i in posicion:
       valor = valor + posicion[i]*valores[i]
    return valor

def pesoTotal(posicion):
    peso = 0
    for i in posicion:
        peso = peso + posicion[i]*pesos[i]
    return peso

