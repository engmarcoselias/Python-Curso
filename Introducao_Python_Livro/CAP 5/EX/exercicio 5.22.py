# Exercicio 5.22


'''Programa que exibe um menu sobre as tabuadas da divisao,
subtração, adição, e multiplicação e uma opçao de sair.E
repete ate que a opção sair seja escolhida'''

tabuada = 0
n1 = 'adição'
n2 = 'subtração'
n3 = 'divisão'
n4 = 'multiplicação'
n5 = 'sair'

while True:
     opção = str(input('Escolha uma opção '))
     if opção == n5:
          break
     elif opção == n1:
          while tabuada <= 10:
               numero = 0
               while numero <= 10:
                    print('%d + %d = %d' % (tabuada, numero, tabuada + numero))
                    numero += 1
               tabuada += 1
     elif opção == n2:
          while tabuada <= 10:
               numero = 0
               while numero <= 10:
                    print('%d - %d = %d' % (numero, tabuada, numero - tabuada))
                    numero += 1
               tabuada += 1

''' Programa imconpleto '''
          
                    

          
     
