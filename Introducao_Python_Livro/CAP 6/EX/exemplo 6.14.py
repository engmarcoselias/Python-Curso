# Pagina 54 PDF
# Exemplo 6.14

'''Programa para adição de elementos a lista'''

# Programa modificado para teste

'''programa que cadastra clientes e atribui um numero de conta
e tem a função de sair se digitar nao e 0 para finalizar
cadastro'''


l = []
x = 0

print('CADASTRO')



n1 = input('Digite SIM para continuar e NÃO para sair: ')

if n1 == 'sim':
    
    while True:
        nomes = str(input('Digite o nome ou 0 para sair: '))
        if nomes == '0':
             break
             
        
        l.append(nomes)# metodo para adicionar um elemento a lista
        x += 1
    total = len(l)   
    n2 = int(input('Para consultar os dados Excolha o'
           ' numero de conta(Total de 0001 a %04d):  '% total))
    print('Numero de conta para %s'
                  ' é  %04d ' % (l[n2 - 1], x))
#Tem um erro na hora de digitar a conta ele mostra o nome escolhido mais o
    #numero total da lista e nao o numero correspondente a conta escolhida.
    
        
elif n1 == 'nao':
    print('Programa Finalizado')

        
