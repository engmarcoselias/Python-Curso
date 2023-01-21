# Exemplo 6.36 pg 61 pdf

'''Programa para ler uma lsita de compras ate se digitar fim'''

compras = []

while True:
    produto = input('Produto ' )
    if produto == 'fim':
        break
    compras.append(produto)
for p in compras:
    print(p)
    
