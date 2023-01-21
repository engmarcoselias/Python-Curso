#Exemplo 6.22 pdf pg 56


'''Programa simulando uma pilha de pratos para lavar'''


prato = 5
pilha = list(range(1, prato + 1))

while True:
    print('\nExistem %d pratos na pilha' % len(pilha))
    print('Pilha atual', pilha)
    print('Digite E para empilhar um novo prato')
    print('Ou D para desempilhar , S para sair.')


    operação = input('Operação (E, D ou S)')
    if operação == 'D':
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print('Prato % lavado' % lavado)
        else:
            print('Pilha vazia! nada para lavar.')
            
    elif operação == 'E':
        prato += 1
        pilha.append(prato)
    elif operação == 'S':
        break
    else:
        print('Operação inválida! Digite apenas E, D ou S!')



             
