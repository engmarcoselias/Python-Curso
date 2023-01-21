#Exercico 4.10

'''Programa para calcular o gasto de energia eletrica de tres tipos de instalacoes, residencia,
comercio, programa le a quantidade de KWH e o tipo de instalacao e da o preco.'''

kwh = float(input('Quantidade de KWH consumidos: '))
tipo = str(input('Tipo da Instalação, r(Residencia), i(Industria), c(Comercio): '))
preco = 0

if tipo == str('r'):
    tipo = str('Residencia')
elif tipo == str('i'):
    tipo = str('Industria')
elif tipo == str('c'):
    tipo = str('Comercio')
    
    

if kwh > 0 and kwh <= 500:
    preco = kwh * 0.40
elif kwh > 500 and kwh < 1000:
    preco = kwh * 0.65
elif kwh == 1000:
    preco = kwh * 0.55
elif kwh > 1000 and kwh < 5000:
    preco = kwh * 0.60
elif kwh == 5000:
    preco = kwh * 0.55
elif kwh > 5000:
    preco = kwh * 0.60
print('O seu tipo de instalação é {}, e o valor cobrado sera de R$ {:.2f}'.format(tipo, preco))# estilo de formatação PYthon mais novo

    
