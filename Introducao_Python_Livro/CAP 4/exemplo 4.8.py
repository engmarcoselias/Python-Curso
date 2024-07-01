# Programa para separar produtos por categoria e colocar o preco
# pag 42 do pdf


#tabela 4.7

#Programa so com IF e ElSE

'''categoria = int(input('Entre com a categoria do produto: '))
if categoria == 1:
    preco = 10.00
else:
    if categoria == 2:
        preco = 18.00
    else:
        if categoria == 3:
            preco = 23.00
        else:
            if categoria == 4:
                preco = 26.00
            else:
                if categoria == 5:
                    preco = 31.00
print('O preco deste produto é: R$ %.2f'% preco)'''
# OBS: o ELSE tem que sempre pertencer a uma iF

# Programa com ELIF

categoria = int(input('Entre com a categoria do produto: '))


if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 18.00
elif categoria == 3:
    preco = 23.00
elif categoria == 4:
    preco = 26.00
elif categoria == 5:
    preco = 31.00
else:
    print('A categoria e invalida digite um valor entre 1 e 5')
    preco = 0
print('O valor deste produto é R$ %.2f' % preco)



             

                
