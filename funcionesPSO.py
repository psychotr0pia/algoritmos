import math
import numpy as np
import random as rnd

def velocidad(velActual, mejorPos, posActual):
    return(masa*velActual + collab*random()(gBest - velActual) + cognitive*random()(mejorPos - posActual))

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

