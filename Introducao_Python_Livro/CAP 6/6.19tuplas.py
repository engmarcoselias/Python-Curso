#criando uma tupla que é imutavel representam valores constantes
#OBS: suporta a maior parte das operações de lista como fatiamento e indexação

tupla = ("a","b","c")
print(tupla)

#tupla com for

for a in tupla:
    print(a)

#tupla sem parenteses (empacotamento)

tupla1 = 100,200,300
print(tupla1)

#desempacotar  valores

a,b,c,d = 100,200,300,400
print(a,b,c,d)

#trocando o valor de variaveis

a,b,c,d = d,c,b,a
print(a,b,c,d)

#quando apenas um valor estiver presente utilizar virgula depois

t1 = (1)
print(t1) #errado vai gerar um valor inteiro ao invez de uma tupla

t1 = (1,)
print(t1)#gera uma tupla


#tupla vazia

t2 = ()
print(t2)

#criando tupla de uma lista

l = [2,3,5,6]
t3 = tuple(l)
print(t3)

#concatenando tuplas

t4 = tupla1 + t3
print(t4)

#tupla contendo um elemento alteravel(ex lista)

t5 = ("a",["b","c","d"])
d = len(t5)
print(d)

t5[1].append("maçã")
print(t5)


