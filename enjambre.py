#!/usr/bin/python3
import funcionesPSO as f
import particula as p

enjambre = []
#Datos PSO
gBest = p.gBest(7)
gBest.llenarCeros()
masa = 0.9
collab = 0.6
cognitive = 0.6
maxIter = 5
popSize = 5
#Datos Mochila
longitud = 7
maxPeso = 15
for i in range(popSize):
    enjambre.append(p.Particula(longitud))
    enjambre[i].llenarCeros()
    enjambre[i].posInicial()
iteracion = 0
while iteracion < maxIter:
    for particula in range(popSize): #se recorre cada particula
        while True: #loopeamos hasta que se logre factibilidad
            enjambre[particula].actualizarVelocidad(gBest) 
            enjambre[particula].actualizarPos()
            if (enjambre[particula].factibilidad() == 1):
                break
        enjambre[particula].mejorpBest()
        if(enjambre[particula].valor() > gBest.valor()):
            enjambre[particula].copyTogBest(gBest)
    iteracion = iteracion + 1
print(gBest.pBest)
