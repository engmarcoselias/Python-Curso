#Exercicio 4.9

'''Escrever um programa para aprovar um emprestimo para compra de casa
o valor da prestação nao pode passar de 30% do salario, o programa deve
perguntar o valor do imovel, o salario , e a quantidade de anos a pagar.'''



valor = float(input('Entre com o valor do imovel: R$ '))
salario = float(input('Entre com o salario: R$ '))
meses = float(input('Entre com a quantidade de meses do financiamento em Mêses: '))
prestacao = valor / meses

if prestacao >= (30*salario)/100:
    print('O valor da prestação de R$ {:.2f} exede o limite de 30% do salario nao e possivel fazer o financiamento'.format(prestacao))
else:
    print('O valor da prestação é R$ {:.2f} e esta dentro do limite de 30% do salario e e possivel liberar o financiamento.'.format(prestacao))


