#Exercicio 6.11 pdf pg 59

'''Programa do exemplo 6.15 editado tirando WHILE e usando For'''

L = []
while True:
     n = int(input("Digite um número (0 sai):"))
     if n == 0:
         break
     L.append(n)
for e in L:
    print(e)
# O primeiro while não pôde ser convertido em for porque
# o número de repetições é desconhecido no início.
