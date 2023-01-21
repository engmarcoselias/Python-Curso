# Exemplo 6.50 pag 66 pdf

''' Programa para obter preço com um dicionario'''


''' Criando um dicionario'''

tabela = { 'Alface' : 0.45,
           'Batata' : 1.20,
           'Tomate' : 2.30,
           'Feijão' : 1.50 }

while True:
    produto = input('Digite o nome do produto, fim para terminar: ')
    if produto == 'fim':
        break
    if produto in tabela:# se o produto   estiver na tabela
        print('Preço %5.2f' % tabela[produto])
    else:
        print('Produto não encontrado')
