#Exercicio 6.17 pag 68 pdf

'''programa da listagem 6.53 editado para entrar com o produto
e a quantidade vendida'''

estoque = {'maçã': [100, 0.70],
           'banana': [200, 0.65],
           'arroz': [25, 10.00],
           'alho': [50, 1.00]}

produto, quantidade = input('Produto: '), int(input('Quantidade: '))
verificação = produto in estoque

if verificação == True:
    valor = estoque[produto][1]
    baixa = estoque[produto][0] - quantidade
    total = quantidade * valor
    print('R$ %.2f total de produtos no estoque %d'% (total, baixa))
else:
    print('Produto não encontrado')

    






