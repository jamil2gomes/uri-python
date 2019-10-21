n100 = n50 = n20 = n10 = n5 = n2 = n1 = m50 = m25 = m10 = m5 = m1 = 0

N = float(input())

centavos = N * 100
n100 = int(N / 100.0)
N %= 100
n50 = int(N / 50.0)
N %= 50
n20 = int(N / 20.0)
N %= 20
n10 = int(N / 10.0)
N %= 10
n5 = int(N / 5.0)
N %= 5
n2 = int(N / 2.0)
N %= 2
n1 = int(N / 1.0)
N %= 1
centavos = int(centavos % 100)
m50 = int(centavos / 50)
centavos %= 50
m25 = int(centavos / 25)
centavos %= 25
m10 = int(centavos / 10)
centavos %= 10
m5 = int(centavos / 5)
centavos %= 5
m1 = int(centavos)

print('''NOTAS:
{:d} nota(s) de R$ 100.00
{:d} nota(s) de R$ 50.00
{:d} nota(s) de R$ 20.00
{:d} nota(s) de R$ 10.00
{:d} nota(s) de R$ 5.00
{:d} nota(s) de R$ 2.00
MOEDAS:
{:d} moeda(s) de R$ 1.00
{:d} moeda(s) de R$ 0.50
{:d} moeda(s) de R$ 0.25
{:d} moeda(s) de R$ 0.10
{:d} moeda(s) de R$ 0.05
{:d} moeda(s) de R$ 0.01
'''.format(n100, n50, n20, n10, n5, n2, n1, m50, m25, m10, m5, m1))
