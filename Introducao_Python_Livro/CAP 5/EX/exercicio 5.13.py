# Exemplo 5.13

'''Programa que pergunta o valor de uma divida e seus  juros e tambem
o valor mensal que sera pago, e mostra o numero de meses para que a
divida seja paga e o total de juros'''
juros2 = 0
x = 0
valor = float(input('O valor da divida: R$ '))
juros1 = float(input('Juros: '))
pago = 0
while valor > 0 :
     p = float(input('Qual o valor pago por mês? R$ '))
     pago = pago + p
     valor = valor - p
     x = x + 1
     juros2 = juros2 + juros1
    


print('A divida sera paga em %s mês(es), a valor pago sera R$ %2.2f, e o total de juros é R$ %2.2f.'% (x, pago, juros2))
       
