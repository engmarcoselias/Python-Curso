# exercicio 4.3 pagina 41 pdf
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite outro numero: '))
if n1 > n2:
    if n1 > n3:
        print('O maior numero é %.1f ' % n1)
if n1 < n2:
    if n1 < n3:
         print('O menor numero é %.1f ' % n1)
if n2 > n1:
    if n2 > n3:
        print('O maior numero é %.1f ' % n2)
if n2 < n1:
    if n2 < n3:
        print('O menor numero é %.1f' % n2)
if n3 > n1:
     if n3 > n2:
         print('O maior numero  é %.1f' % n3)
if n3 < n1:
    if n3 < n2:
        print('O menor numero é %.1f' % n3)
