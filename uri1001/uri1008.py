number = int(input())
horasTrabalhadas = int(input())
valorPorHora = float(input())

salario = horasTrabalhadas * valorPorHora

print("NUMBER = {:d}".format(number))
print("SALARY = U$ {:.2f}".format(salario))