qte = int(input())
sim = 0
nao = 0

for i in range(qte):
    valor = int(input())
    if 10 <= valor <= 20:
        sim += 1
    else:
        nao += 1

print("{:d} in".format(sim))
print("{:d} out".format(nao))
