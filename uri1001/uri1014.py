totalPercorrido = int(input())
totalCombustivelGasto = float(input())

consumo = totalPercorrido / totalCombustivelGasto
print("{:0.3f} km/l".format(consumo))
