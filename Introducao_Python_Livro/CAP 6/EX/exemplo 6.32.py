#exemplo 6.32 pg 60 pdf

'''Usando enumerate que é um gerador que retorna a cada interação do laço FOR uma tupla diferente para  mostrar o indice e o
elemeto de uma lista'''

l = [5, 9, 13]
for x, v in enumerate(l): # gerando tupla o primeiro e o indice e o segundo elemento da lista na função for
    print('[%d] %d'%(x, v), end=',')# %d e um numero inteiro e end e para nao mudar de linha
