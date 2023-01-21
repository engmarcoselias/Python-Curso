# Programa para calcular preço de uma viagem com KM ate 200 valor 0.50
# e acima de 200 0.45
#

km = float(input('Distancia percorrida em KM é ? '))
valor = 0
if km >= 200:
    valor = valor + (0.50*km)
else:
     valor = valor +(0.45*km)
print('O valor cobrado pela viagen é: R$ %.2f' % valor)
