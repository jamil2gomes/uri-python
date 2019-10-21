anos = meses = dias = 0

a = int(input())

anos = int(a / 365)
meses = int((a % 365) / 30)
dias = int((a % 365) % 30)

print("{:d} ano(s)\n"
      "{:d} mes(es)\n"
      "{:d} dia(s)".format(anos, meses, dias))
