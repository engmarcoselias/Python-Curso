#--------------------------------NUMEROS EM PYTHON-------------------------------------

#Existem três tipos numéricos em Python:

#int
#float
#complex

#Variáveis ​​de tipos numéricos são criadas quando você atribui um valor a elas.

#EX:

x = 1   #int
y = 2.8 #float
z = 1j  #complex


#Inteiro
#Int, ou inteiro, é um número inteiro, positivo ou negativo, sem decimais, de comprimento ilimitado.

#EX

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


#Float

#Float, ou "número de ponto flutuante" é um número, positivo ou negativo, contendo uma ou mais casas decimais.

#EX:

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#Float também pode ser um número científico com um "e" para indicar a potência de 10.

#EX:

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#Complexo
#Números complexos são escritos com um "j" como parte imaginária:

#EX:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


#Conversão de tipo
#Você pode converter de um tipo para outro com os métodos int(), float(), e complex():

#Exemplo:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

'''Observação: não é possível converter números complexos em outro tipo de número.'''

#úmero aleatório
#O Python não tem uma random()função para criar um número aleatório, mas tem um módulo interno chamado randomque pode ser usado para criar números aleatórios:

#Exemplo:

#Importe o módulo aleatório e exiba um número aleatório entre 1 e 9:

import random

print(random.randrange(1, 10))