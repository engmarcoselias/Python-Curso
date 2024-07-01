# Exercicio 5.15 PG 49 pdf

'''Programa para controlar uma caixa registradora, o usuario deve digitar
o codigo do produto e a quantidade comprada'''



'''tabela de precos de acordo com codigo
1 = 0.50
2 = 1.00
3 = 4.00
5 = 7.00
9 = 8.00  '''



c1 = '1'
c2 = '2'
c3 = '3'
c4 = '5'
c5 = '9'
c6 = '0'
total = 0
while True:
     codigo = str(input('Codigo do produto: '))
     if codigo != '1' and codigo != '2' and codigo != '3' and codigo != '5' and codigo != '9' and codigo != '0':
          print('Codigo Invalido.')
     elif codigo == c6:
          break
     
     elif codigo == c1:
          quantidade = int(input('Quantidade: '))
          preco1 = 0.50 * quantidade
          total = total + preco1
     elif codigo == c2:
          quantidade = int(input('Quantidade: '))
          preco2 = 1.00 * quantidade
          total = total + preco2
     elif codigo == c3:
          quantidade = int(input('Quantidade: '))
          preco3 = 4.00 * quantidade
          total = total + preco3
     elif codigo == c4:
          quantidade = int(input('Quantidade: '))
          preco4 = 7.00 * quantidade
          total = total + preco4
     elif codigo == c5:
          quantidade = int(input('Quantidade: '))
          preco5 = 8.00 * quantidade
          total = total + preco5  
print('R$ %.2f '% total)
          
