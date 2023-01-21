#Exemplo 6.21  pg 57 pdf


'''Programa de uma fila de banco '''


'''Usando o elemento POP para retornar o valor do elemento e o
e o apagar da lista'''


ultimo = 10


fila = list(range(1, ultimo + 1))



while True:
    print('\n\nExistem %d clientes na fila' % len(fila))#\n e para pular linhas
    print('Fila atual:',fila)                   #len mostra a quantidade de elementos na lista
    print('Digite F para adicionar um cliente ao fim da fila.')
    print('Ou A para realizar o atendimento. S para sair.')

    operação = input('Operação (F, A ou S):')
    if operação == 'A':

        
        if(len(fila)) >0:
            atendido = fila.pop(0)# o elemento pop mostra o valor elemento e o retira da lista
            print('Cliente %d atendidio'% atendido)
        else:
            print('Fila vazia! Ninguem para atender.')

            
    elif operação == 'F':
        ultimo += 1  #incrementa o tickt do novo cliente(muda o valor de ultimo para +1)
        fila.append(ultimo) #adiciona um elemento a lista
    elif operação == 'S':
        break
    else:
        print('Operação Inválida: Digite apenas F, A ou S!')
        
        
        


   
