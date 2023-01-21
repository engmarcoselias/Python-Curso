#Exemplo 6.43 pag 62 pdf

'''Programa para imprimir uma lista de compras'''

compras = []

while True:
    produto = str(input('Produto: '))
    if produto == 'fim':
        break
    quantidade = int(input('Quantidade: '))
    preço = float(input('Preço: '))
    compras.append([produto, quantidade, preço])# adiciona os valores a lista compras
soma = 0.0
for e in compras:
    print('%20s x %d  R$%6.2f' % (e[0], e[1], e[2]))
    soma += e[1] * e[2]
print('Total: %2.2f' % soma)
