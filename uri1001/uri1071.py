valor1 = int(input())
valor2 = int(input())

soma = 0

if valor1 > valor2:
    i = valor1 - 1
    while i > valor2:
        if i % 2 != 0:
            soma += i
        i -= 1
    else:
        i = valor2 - 1
        while i > valor1:
            if i % 2 != 0:
                soma += 1
            i -= 1

print(soma)
