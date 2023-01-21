#Exercicio 6.2 pdf pagina 54

'''exercicio 6.2 imcremetado para adicionar valores as duas listas atraves de
input e juntar as duas listas em uma terceira'''

lista1 = []
lista2 = []
lista3 = []


while True:
    operação = str(input('\nDigite  1 para (LISTA 1) ou 2 para (LISTA 2) , ou S para sair    '))
    if (operação == 's') or (operação == 'S'): # se o valor da entrada for 's' minusculo ou maisculo parara o programa e mostra a lista tres que é uma 
        lista3 = lista1 + lista2                #soma das listas 1 e 2
        print('\nLISTA 3', lista3)
        break
    
    elif operação == '1':
        print('\n\nLISTA selecionada!')
        l1 = 0
        while (l1 != 'voltar') and (l1 != 'VOLTAR'):# para o laço continuar a entrada tem que ser diferente de 'voltar' MINUSCULO OU MAISCULO
            l1 = input('\nDigite um valor para adicionar ou ''voltar'' para o menu anterior:   ')
        
            lista1.append(l1) # adiciona valor a lista 

        if lista1 == []:        #se a lista estiver vazia para nao dar erro no programa adicionar um valor que sera retirado em seguida pelo comando 'del'
            lista1.append(1)
        del lista1[-1]          #parte do programa para retirar o ultimo valor da lista que e o comando voltar ou um valor so para nao dar erro
        print('\nLISTA 1',lista1)
        
    elif operação == '2':
        print('\n\nLISTA selecionada!\n\n')
        l2 = 0
        while (l2 != 'voltar') and (l2 != 'VOLTAR'):
            l2 = input('\nDigite um valor para adicionar ou ''voltar'' para o menu anterior:    ')

            lista2.append(l2)
        if lista2 == []:
            lista2.append(1)
        del lista2[-1]
        print('\nLISTA 2', lista2)
            
        
    


