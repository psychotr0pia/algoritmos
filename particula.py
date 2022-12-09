import funcionesPSO as f
import random as rnd
maxPeso = 15
class gBest:
    def __init__(self, lenVector):
        self.pos = []
        self.vel = []
        self.pBest = []
        self.lenVector = lenVector
    def llenarCeros(self):
        for i in range(self.lenVector):
            self.pos.append(0)
            self.vel.append(0)
            self.pBest.append(0)
    def valor(self):
            return f.funcionObjetivo(self.pos)
    

class Particula:
    def __init__(self, lenVector):
        self.pos = []
        self.vel = []
        self.pBest = []
        self.lenVector = lenVector
    def llenarCeros(self):
        for i in range(self.lenVector):
            self.pos.append(0)
            self.vel.append(0)
            self.pBest.append(0)
    def posInicial(self):
        for i in range(self.lenVector):
            self.pos[i] = rnd.randint(0, 1)
    def copiarPBest(self):
        for i in range(self.lenVector):
            self.pBest[i] = self.pos[i]
    def factibilidad(self):
        if(f.pesoTotal(self.pos) > maxPeso):
            return 0
        else:
            return 1
    def peso(self):
        return f.pesoTotal(self.pos)
    def valor(self):
        return f.funcionObjetivo(self.pos)
    def mejorpBest(self):
        if(self.peso() > f.funcionObjetivo(self.pBest)):
            self.copiarPBest()
            return 1
        else:
            return 0
    def actualizarVelocidad(self, gBest):
        for i in range(self.lenVector):
            self.vel[i] = f.velocidad(self.vel[i], self.pBest[i], self.pos[i], gBest.pos[i])
    def actualizarPos(self):
        for i in range(self.lenVector):
            if (rnd.randint(0,1)< f.sigmoide(self.vel[i])):
                self.pos[i] = 1
            else:
                self.pos[i] = 0
    def copyTogBest(self, gBest):
        for i in range(self.lenVector):
            gBest.pos[i] = self.pos[i]
            gBest.vel[i] = self.vel[i]
            gBest.pBest[i] = self.pBest[i]










