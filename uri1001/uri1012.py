valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c)) / 2
circulo = pi * (pow(float(c), 2))
trapezio = float(c) * (float(a) + float(b)) / 2
quadrado = pow(float(b), 2)
retangulo = float(a) * float(b)

print("TRIANGULO: {:.3f}"
      "\nCIRCULO: {:.3f}"
      "\nTRAPEZIO: {:.3f}"
      "\nQUADRADO: {:.3f}"
      "\nRETANGULO: {:.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo))
