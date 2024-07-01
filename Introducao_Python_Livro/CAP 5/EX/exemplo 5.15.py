# Exemplo 5.15

'''Tabuada de 1 a 10'''


tabuada = 1

while tabuada <= 10:
     numero = 1
     while numero <= 10:
          print('%d X %d = %d' %(tabuada, numero,
                                 tabuada * numero))
          numero += 1
     tabuada += 1
