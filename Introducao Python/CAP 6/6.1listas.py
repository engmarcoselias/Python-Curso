l = [12,15,3,45]

print(l)

#6.1Indice de uma lista

print(l[3])

#6.2copiando uma lista
v = l
print(v)

#6.2alterando (v tambem altera l)

v[0] = 2
print(v)
print(l)

#6.2fatiamento de lista
r = l[:-2]
print(r)

#6.3tamanho da lista
print(len(l))

#6.4adicionar elementos a lista com .append

l.append('a')
print(l)

#6.4adicionando elemento a lista

l +=[3]
print(l)

#6.5remoção de elementos da lista

del l[4]
print(l)

#6.6criando lista com range
l2 = list(range(50,60))
print(l2)

#remoção de fatias
l2 = list(range(101))
del l2[1:99]
print(l2)

#6.6lista com filas retirando da lista com pop
l3 = [1,2,3,4,5,6]
l3.append(2)
print(l3)

deletado = l3.pop(0)
print(deletado)

'''#6.8pesquisa na lista EX.

a = [2,5,8,7]
p = int(input("digite o valor a ser procurado: "))

achou = False
x = 0
while x <len(a):
    if a[x] == p:
        achou = True
        break
    x += 1
if achou:
    print("%d achado na posição %d" %(p,x))
else:
    print("Não encontrado")'''

#6.9usando for

for a in l2:
    print(a)

#6.10usando range

for v in range(10):
    print(v)

#6.9usando range com salto

for t in range(3,33,3):
    print(t,end="27")
print()

#6.9range em uma lista

b = list(range(10,120,10))
print(b)

#6.11função enumerate gera uma tupla

b = [5,6,8,9,4]

for x, e in enumerate(b):
    print("[%d] %d"%(x,e))

#6.14lista dentro de lista com string aessando letra

s = ["maçã","banana","laranja"]
print(s[0])
print(s[0][1])



