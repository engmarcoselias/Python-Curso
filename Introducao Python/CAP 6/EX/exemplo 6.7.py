# Exemplo 6.7

'''Programa para ler 5 numeros, armazenalos e depois solicite que o usuario
escolha um para ser mostrado, e se digitar 0  saia do programa'''


z = [0,0,0,0,0]
x = 0


while x < 5:
    z[x] = int(input('Entre com um numero %d: '%(x + 1)))
    x += 1
while True:
    escolha = int(input('Que posição você quer imprimir?( Digite 0 para sair): '))
    if escolha == 0:
        break
    print('A posição escolhida foi %d.' % (z[escolha - 1]))
    
