# Exercicio 5.9

'''programa para ler dois numeros e mostre a divisao do primeiro pelo
segundo, so utilizando as operaçoes de some e subtração'''


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

vezes = 0
resto = n1

while resto >= n2:
     resto = resto - n2
     vezes = vezes + 1
print('O numero %d dividido por %d e igual a %d e o resto da divisão é %d' % (n1, n2, vezes, resto))
     
     
     

