# Exemplo 5.13  pag 47

'''Programa para interromper repetição'''


s = 0

while True:
     v = int(input('Digite um numero a somar ou digite 0 para'
                   ' sair: '))
     if v == 0:
          break
     s = s + v
     print(s)
     
