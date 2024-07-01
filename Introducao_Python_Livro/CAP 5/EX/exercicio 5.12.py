# Exercicio 5.12

'''Programa do 5.11 alterado para adicionar um deposito mensal e calcular
os juros en cima do novo valor'''


x = 0
taxa = float(input('Taxa de juros: '))
deposito = float(input('Deposito inicial: R$ '))
 

while x < 24:
     x = x + 1
     mes = float(input('Valor do deposito do  %s mês: R$ '% x))
     deposito = ((deposito + mes) * taxa/100) + deposito + mes
     print('R$ %2.2f'%deposito)

     
print('O total de ganho no periodo com correção de juros é R$ %2.2f '
      % deposito)
