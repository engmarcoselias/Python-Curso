# exemplo 6.33 pag 61 pdf

'''Verindicar o maior valor'''

l = [-1, 7, 2, -10]

maximo = l[0]  # a variavel maximo pega o valor de l [0]
for v in l:     # o laço for adiciona a variavel v os valores da lista um a um
    if v < maximo: # a condição if verifica se v e menor q maximo 
        maximo = v # se for verdade o valor da variavel maximo muda para o valor de v 
print(maximo)

