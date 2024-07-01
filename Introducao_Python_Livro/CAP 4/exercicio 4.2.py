veloci = float(input('Qual a velocidade o carro estava? '))
if veloci > 80:
    print('Voce foi multado por ultrapassar o limite de velocidade que é 80Km/h')
    multa = (veloci-80)# variavel para encontrar o km excedente
    print('Você estava a %.1f Km acima da velocidade permitida sua multa e no valor de R$ %.2f'%(multa, multa*5)) 
if veloci < 39:
    print('Você esta muito lento para esta via')
if veloci <= 80  and veloci >= 40:
    print('Voce esta dentro do limite de velocidade Parabêns!')
