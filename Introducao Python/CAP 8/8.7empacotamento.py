#8.28empacotamento de paramentros em uma lista

def soma(a,b):
    print(a+b)
L = [2,3]
soma(*L)#asterisco utilizado para desempacotar a lista

#8.29 outro exemplo de empacotamento

def barra(n=10,c="'"):
    print(c*n)
l = [[5,"'"],[10,"'"],[5],[6,"'"]]
for e in l:
    barra(*e)

#8.30 som\ com numeros indeterminados de parametros

def soma(*args):
    s = 0
    for x in args:
        s += x
    return s
print(soma(1,2))
print(soma(2))
print(soma(5,6,7,8))
print(soma(9,10,20,30,40))

a = [2,5,6,3]
print(a)

a = [2,5,6,3]
print(*a)