#!/usr/bin/python3
import funcionesPSO as f
import particula as p

enjambre = []
#Datos PSO
gBest = p.gBest(6)
gBest.llenarCeros()
masa = 1
collab = 2
cognitive = 2
maxIter = 5
popSize = 5
#Datos Mochila
longitud = 6
maxPeso = 8
valores = [2,5,6,10,13,16]
pesos = [1,2,4,5,7,8]
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
    print(gBest.pos)
    iteracion = iteracion + 1
