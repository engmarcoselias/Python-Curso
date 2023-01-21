valor = float(input('Entre com o preço da mercadoria R$ '))
desconto = float(input('Entre com a porcentagem de desconto: '))
preco = valor*desconto/100
print('O valor da mercadoria é R$ %.2f, e com o desconto de R$ %.2f o valor passa a ser R$ %.2f.'%(valor, preco, valor-preco))
