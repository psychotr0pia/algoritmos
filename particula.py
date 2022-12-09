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
        if(pesoTotal(self.pos) > maxPeso):
            return 0
        else:
            return 1
    def peso(self):
        return pesoTotal(self.pos)
    def valor(self):
        return funcionObjetivo(self.pos)
    def mejorpBest(self):
        if(self.peso > funcionObjetivo(self.pBest)):
            self.copiarPBest()
    #metodo para actualizar velocidades
    #metodo pa calcular nueva pos
