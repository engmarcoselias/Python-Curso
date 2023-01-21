#8.1definindo uma nove função

def soma(a,b):
    print(a+b)
soma(2,3)

#8.2retornando valores

def soma(a,b):
    return(a+b)
print(soma(2,9))

#8.3retornar se o valro e par ou impar

def épar(x):
    return(x%2 == 0)
print(épar(2))
print(épar(5))

#8.4reutilização da função ápr em outra fução

def par_ou_impar(x):
    if épar(x):#se True
        return "par"
    else:
        return "impar"
    '''OBS: A instrução return faz com que a função pare de executar e que o valor reorne imediatamente ao programa ou a função que o chamou seguido do retorno do valor. As linhas da função apos a instrução return são iguinoradas de forma similar a instrução break no while ou for(interrupção da execução da função)'''
print(par_ou_impar(2))
print(par_ou_impar(5))

#função de pesquisa em uma lsita

def pesquisa(lista,valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
    return None
L = [10,20,25,30]
print(pesquisa(L,25))
print(pesquisa(L,27))

#calcula da media de uma lista

def soma(L):
    total = 0
    for e in L:
        total += e
    return total
def media(L):
    return(soma(L)/len(L))

#calculo de fatorial

def fatorial(n):
    fat = 1
    while n> 1:
        fat *= n
        n -= 1
    return fat
print(fatorial(0))

#funçoes para calcular soma maximo e minimo de uma lista

l = [5,7,8]
print(sum(l))#soma

print(max(l))#maximo

print(min(l))
    