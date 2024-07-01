# Exemplo 5.16

'''O mesmo programa do exemplo 5.15 sem repetiçoes aninhadas'''



tabuada = 1
numero = 1


while tabuada <= 10:
     print('%d X %d = %d' %(tabuada, numero, tabuada * numero))
     numero += 1
     if numero == 11:
          numero = 1
          tabuada += 1
