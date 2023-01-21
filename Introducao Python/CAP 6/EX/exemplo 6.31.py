# exemplo 6.31 pag 60

''' impressão de indices sem usar enumerate'''

l = [5, 9, 13]
x = 0
for v in l:
    print('[%d] %d' % (x, v))
    x += 1
