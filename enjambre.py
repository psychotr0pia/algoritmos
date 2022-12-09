#!/usr/bin/pyton3
import funcionesPSO
import particula
import math
import numpy as np

enjambre = []
#Datos PSO
gBest = Particula(6)
masa = 1
collab = 2
cognitive = 2
maxIter = 1
#Datos Mochila
longitud = 6
maxPeso = 8
valores = [2,5,6,10,13,16]
pesos = [1,2,4,5,7,8]
for i in range(popSize):
    print(i)
    enjambre.append(Particula())
    enjambre[i].llenarCeros()
    enjambre[i].posInicial()
iter = 0
while iter < maxIter:
    for particula in range(popSize): #se recorre cada particula
        for dim in range(longitud): #se recorre cada dimension de la particula
            while(enjambre[particula].factibilidad != 1):
                enjambre[particula].posInicial()
            enjambre[particula].vel[dim]
