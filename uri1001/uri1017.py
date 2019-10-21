horasGastas = int(input())
velocidadeMedia = int(input())

distancia = float(horasGastas * velocidadeMedia)
quantidadeLitros = distancia / 12

print("{:.3f}".format(quantidadeLitros))
