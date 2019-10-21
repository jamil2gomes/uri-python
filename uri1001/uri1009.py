nome = str(input())
salarioFixo = float(input())
totalDeVendas = float(input())

comissao = (totalDeVendas * 15)/100
salario = comissao + salarioFixo

print("TOTAL = R$ {:.2f}".format(salario))