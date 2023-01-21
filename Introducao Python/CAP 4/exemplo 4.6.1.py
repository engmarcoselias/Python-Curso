# Exemplo de aninhar
# calculo de uma conta de telefone


minutos = int(input('Quantos minutos vc utilizou este mês: '))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15
print('Voce vai pagar este mês R$ %6.2f'% (minutos * preco))
