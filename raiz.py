def funcion(numero, x):
    return (0.5*(x + (numero)/(x)))
numero = 7
inicio = 1

for i in range(7):
    inicio = funcion(numero, inicio)
    print(inicio)


