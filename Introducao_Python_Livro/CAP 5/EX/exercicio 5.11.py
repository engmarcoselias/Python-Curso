# Exercicio 5.11

'''Programa que vai ler o valor do deposito de um individuo e a taxa
de juros de sua poupança, e vai exibir os valores dos mês a mês para
os 24 primeiros meses e escreva o total nesse periodo'''

x = 0
taxa = float(input('Taxa de juros: '))
deposito = float(input('Entre com o valor de deposito inicial: '))
n = (taxa/100) * deposito



while x < 24:
     deposito = deposito + n
     x = x + 1
     print('O valor do %2.0d mês é : %2.2f'% (x, deposito))

print('O valor total com a correção de juros no periodo é de %2.2f.'% deposito)
     
