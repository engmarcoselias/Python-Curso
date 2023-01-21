# Exemplo 5.11

'''Programa para fazer a soma de 10 numeros'''


n = 1
soma = 0

while n <= 10:
     x = int(input('Digite o %dºnumero: '% n))
     soma = soma + x # acumulador
     n = n + 1 # contador
print('Soma: %d' % soma)
     
