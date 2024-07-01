# exemplo 6.34 pg 61 pdf

'''Programa para separar itens de uma lista e adicionar a outras  duas sendo uma impar
e a outra par'''


v = [3, 5, 6, 90, 34, 7, 63, 8]
p = []
i = []

for a in v:
    if a % 2 == 0:
        p.append(a)
    else:
        i.append(a)
        
print('Pares', p)
print('Impares', i)

