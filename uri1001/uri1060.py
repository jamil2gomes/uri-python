lista = []
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))

positivos = 0

for v in lista:
    if v > 0:
        positivos += 1

print("{:d} valores positivos".format(positivos))
