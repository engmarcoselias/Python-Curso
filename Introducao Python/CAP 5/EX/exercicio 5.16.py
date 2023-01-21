# Exemplo 5.14
# Exercicio 5.16
# Exercicio 5.17
# Exercicio 5.18
# Exercicio 5.19


''' Programa para ler um valor e que mostre a quantidade de
cedulas para pagar este valor(utilizando cedulas de 50, 20
10, 5, 1'''


valor = float(input('Digite um valor a pagar R$ '))
cedulas = 0
atual = 100
apagar = valor


while True:
     if atual <= apagar:
          apagar -= atual
          cedulas += 1
     else:
          print('%d cedula(s) de R$ %.2f' %(cedulas, atual))
          if apagar == 0:
               break
          if atual == 100:
               atual = 50
          elif atual == 50:
               atual = 20
          elif atual == 20:
               atual = 10
          elif atual == 10:
               atual = 5
          elif atual == 5:
               atual = 1
          elif atual == 1:
               atual = 0.50
          elif atual == 0.50:
               atual = 0.10
          elif atual == 0.10:
               atual = 0.05
          elif atual == 0.05:
               atual = 0.02
          elif atual == 0.02:
               atual = 0.01

          cedulas = 0



