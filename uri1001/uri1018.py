n100 = n50 = n20 = n10 = n5 = n2 = 0
n1 = 1

qtd = int(input())
valor = qtd
n100 = int(qtd / 100)
qtd %= 100
n50 = int(qtd / 50)
qtd %= 50
n20 = int(qtd / 20)
qtd %= 20
n10 = int(qtd / 10)
qtd %= 10
n5 = int(qtd / 5)
qtd %= 5
n2 = int(qtd / 2)
qtd %= 2
n1 = qtd

print(valor)
print("{:d} nota(s) de R$ 100,00".format(n100))
print("{:d} nota(s) de R$ 50,00".format(n50))
print("{:d} nota(s) de R$ 20,00".format(n20))
print("{:d} nota(s) de R$ 10,00".format(n10))
print("{:d} nota(s) de R$ 5,00".format(n5))
print("{:d} nota(s) de R$ 2,00".format(n2))
print("{:d} nota(s) de R$ 1,00".format(n1))
