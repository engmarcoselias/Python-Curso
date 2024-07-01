#Exemplo 6.51 pag 67 pdf

'''Excluindo uma chave do dicionario'''


''' Criando um dicionario'''

tabela = { 'Alface' : 0.45,
           'Batata' : 1.20,
           'Tomate' : 2.30,
           'Feijão' : 1.50 }

print(tabela)
del tabela['Tomate']
print(tabela)
