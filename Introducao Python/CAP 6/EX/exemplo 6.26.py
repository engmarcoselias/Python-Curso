#Exemplo 6.26 pdf pg 59


'''programa para pesquisar uma lista usando a instrução for'''



l = [5,6,3,8,7,45]

p = int(input('digite um numero a pesquisar: '))
for e in l:
    if e == p:
        print('Elemento encontrado')
        break
else:
    print('Elemento nao encontrado')
