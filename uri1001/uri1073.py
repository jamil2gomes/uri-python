valor = int(input())

contador = 2

while contador <= valor:
    print("{:d}^2 = {:d}".format(contador, (contador ** 2)))
    contador += 2
