# Exemplo 6.15
 # Pag 54 pdf


'''Programa para adição de elementos a lista'''


l = []

while True:
    n = int(input('Digite um numero(0 sai): '))
    if n == 0:
        break
    l.append(n)


    x = 0
while x <  len(l):
    print(l[x])

    x += 1

