A = input() #nome
B = float(input()) #salario fixo
C = float(input()) #total das vendas efetuadas por mês
TOTAL = ((C*15)/100) + B
print("TOTAL = R$ {:.2f}".format(TOTAL))

