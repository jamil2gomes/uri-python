n = int(input())
horas = int(n / 3600)
minutos = int((n % 3600) / 60)
seg = int((n % 3600) % 60)

print("{:d}:{:d}:{:d}".format(horas, minutos, seg))
