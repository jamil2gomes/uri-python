salario = float(input())

if salario > 4500.00:
    desconto = ((salario - 4500.00) * 0.28) + 350.00
    print('R$ %.2f' % desconto)

if 3000.00 < salario <= 4500.00:
    desconto = ((salario - 3000.00) * 0.18) + 80.00
    print('R$ %.2f' % desconto)

if 2000.00 < salario <= 3000.00:
    desconto = ((salario - 2000.00) * 0.08)
    print('R$ %.2f' % desconto)

if salario <= 2000.00:
    print('Isento')