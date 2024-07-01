#Exemplo 6.53 pag 67 pdf

'''Exemplo de dicionario com estoque e operação de vendas'''


estoque = {'tomate' : [1000, 2.30], 
           'alface' : [ 500, 0.45],
           'batata' : [2001, 1.20],
           'feijão' : [ 100, 1,50]}

venda = [['tomate', 5], ['batata', 10], ['alface', 5]]# atribui a vendas uma lista com o valor da chave do dicionario e um valor que vai multiplicar o produto
total = 0
print('vendas:\n')
for operação in venda: # adiciona a variavel operação valores contidos em venda um por vez 
    produto, quantidade = operação # adicionar um valor a produto e outro a quantidade
    preço = estoque[produto][1]# a variavel preço vai receber o valor de acordo chave de estoque atribuida a variavel produto na posição 1 
    custo = preço * quantidade
    print('%12s: %3d x %6.2f = %6.2f' %
          (produto, quantidade, preço, custo))
    estoque[produto][0] -= quantidade # retira o valor atribuido a variavel quantidade da posição 0 do estoque referente a chave atribuida a variavel produto
    total += custo #adiciona  o valor da variavel custo ao total
    print('Custo total: %21.2f\n' %total)
    print('Estoque:\n')# \n e para pular linha
    
    for chave, dados in estoque.items():
        print('Descrição: ',chave)
        print('Quantidade: ', dados[0])
        print('Preço: %6.2f\n' % dados[1])



