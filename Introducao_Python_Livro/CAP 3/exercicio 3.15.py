cigarros = float(input('Entre com a quantidade de cigarros fumados por dia: '))
anos = float(input('Quantos anos você fumou? '))
dias = (365*(cigarros*10))/1440# o 1440 e a conversão de dia para minutos
print('Um fumante que fumou %.0f cigarros por dia durante %.0f anos perdeu %.f Dias de vida'%(cigarros, anos, dias))
