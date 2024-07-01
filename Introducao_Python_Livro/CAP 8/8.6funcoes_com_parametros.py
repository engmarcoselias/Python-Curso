#8.26função com parametro

def soma(a,b):
    return a+b
def subtração(a,b):
    return a-b
def imprime(a,b,foper):
    print(foper(a,b))
imprime(5,4,soma)
imprime(10,1,subtração)#passar funções com parametro não utiliza ()

#configuração de funções com funções

def imprime_lista(L, finpressao, fcondicao):
    for e in L:
        if fcondicao(e):
            finpressao(e)
def imprime_elemento(e):
    print("Valor: %d"% e)
def epar(x):
    return x % 2 == 0
def impar(x):
    return not epar(x)
L = [1,7,9,2,11,9]
imprime_lista(L,imprime_elemento,epar)
imprime_lista(L,imprime_elemento,impar)
