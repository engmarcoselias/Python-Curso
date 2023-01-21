#Exemplo 6.42 pag 62 pdf

'''Programa com listas dentro de listas'''

produto1 = ['maçã', 10, 3.30]

produto2 = ['pera', 5, 0.75]

produto3 = ['kiwi', 4, 0.98]

compras = [produto1, produto2, produto3]

for e in compras:       # adicionar o valor da lista compras a variavel e
    print('Produto: %s' % e[0]) #%s string
    print('Quantidade: %d' % e[1])#%d numero inteiro
    print('Valor: R$%5.2f' % e[2])# o 5 e distancia antes do ponto e o 2 casas depois do ponto
    

