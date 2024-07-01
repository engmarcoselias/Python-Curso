# Exemplo 6.6

'''Programa do exemplo 6.5 modificado para ler as notas uma a uma '''



notas = [0,0,0,0,0]
soma = 0
x = 0


while x < 5:
    notas[x] = float(input('Nota %d:' % (x + 1)))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print('Nota %d: %.2f' %(x + 1 , notas[x]))
    x += 1
print('Média: %.2f '% (soma/x))


