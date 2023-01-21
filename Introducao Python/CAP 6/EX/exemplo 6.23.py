#Exemplo 6.23 pdf pg 58

'''Programa de uma pesquisa sequencial de um elemento em uma lista'''


l =[12,56,23,58,99]


p = int(input('Digite o valor procurado: ')) # o valor tem que ser estipulado do tipo inteiro se não fica como str e não vai encontrar o valor
achou = False #1 variavel do tipo logico boleano TRUE ou FALSE

x = 0 #contador
while x < len(l):
    if l[x] == p:
        achou = True #2
        break #3
    x += 1
if achou: #4 verificamos o valor da variavel
    print('%d achou na posição %d.' % (p, x))
else:
    print('%d não encontrado' % p)
