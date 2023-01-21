# Exercicio 5.14 PG 49 pdf

'''Programa para ler numeros inteiros ate q o usuario digite 0 e como
resultado mostre a quantidade de numeros digitados a soma e a media
aritimetica'''


x = 0      
soma = 0
print('O primeiro número tem que ser diferente de 0.')

while True:
     n2 = int(input('Digite um número: '))
     if n2 == 0:
          break
     soma = soma + n2
     x = x + 1
media = soma / x

print('O usuario digitou a quantidade de {} números, a soma de todos'
     ' é {:.2f}, e a média é {:.2f}'.format(x, soma, media))
