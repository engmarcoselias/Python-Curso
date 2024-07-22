#------------------------CONTINUAÇÃO DE LISTAS-------------------------#


#--------------------------LISTAS DE LOOPS----------------------------#


#Percorrer uma lista
#Você pode percorrer os itens da lista usando um for loop:

#Exemplo
#Imprima todos os itens da lista, um por um:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Loop pelos números de índice
#Você também pode percorrer os itens da lista consultando seu número de índice.

#Use as funções range()e len()para criar um iterável adequado.

#Exemplo
#Imprima todos os itens consultando seu número de índice:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  #O iterável criado no exemplo acima é [0, 1, 2].


#Usando um loop While
#Você pode percorrer os itens da lista usando um whileloop.

#Use a len()função para determinar o comprimento da lista, comece em 0 e percorra os itens da lista consultando seus índices.

#Lembre-se de aumentar o índice em 1 após cada iteração.

#Exemplo
#Imprima todos os itens, usando um whileloop para percorrer todos os números de índice

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#Looping usando compreensão de lista
#A Compreensão de Lista oferece a sintaxe mais curta para percorrer listas:

#Exemplo
#Um pequeno forloop manual que imprimirá todos os itens em uma lista:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#-------------COMPREENSÃO DE LISTA-------------------#

#Compreensão de lista

#A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente.

#Exemplo:

#Com base em uma lista de frutas, você quer uma nova lista, contendo apenas as frutas com a letra "a" no nome.

#Sem compreensão de lista, você terá que escrever uma fordeclaração com um teste condicional dentro:


#Exemplo

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#Com a compreensão de lista você pode fazer tudo isso com apenas uma linha de código:

#Exemplo

fruits = ["apple","banana","cherry", "kiwi","mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#A Sintaxe

#newlist = [expression for item in iterable if condition == True]

#O valor de retorno é uma nova lista, deixando a lista antiga inalterada.

#Condição

#A condição é como um filtro que aceita apenas os itens que valem True.

#Exemplo
#Aceite apenas itens que não sejam "apple":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

#A condição if x != "apple"  retornará Truepara todos os elementos, exceto "maçã", fazendo com que a nova lista contenha todas as frutas, exceto "maçã".

#A condição é opcional e pode ser omitida:

#Exemplo
#Sem if declaração:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)


#Iterável

#O iterável pode ser qualquer objeto iterável, como uma lista, tupla, conjunto etc.

#Exemplo

# Você pode usar a range()função para criar um iterável:

newlist = [x for x in range(10)]

print(newlist)


#Mesmo exemplo, mas com uma condição:

#Exemplo

#Aceite apenas números menores que 5:

newlist = [x for x in range(10) if x < 5]

print(newlist)


#Expressão

#A expressão é o item atual na iteração, mas também é o resultado, que você pode manipular antes que ele termine como um item de lista na nova lista:

#Exemplo

#Defina os valores na nova lista para letras maiúsculas:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#Você pode definir o resultado como quiser:

#Exemplo

#Defina todos os valores na nova lista como 'hello':

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

#A expressão também pode conter condições, não como um filtro, mas como uma forma de manipular o resultado:

#Exemplo
#Retorne "laranja" em vez de "banana":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

'''A expressão no exemplo acima diz:

"Devolva o item se não for banana, se for banana devolva laranja".'''



#----------------LISTAS DE CLASSIFICAÇÃO(SORT LIST)---------------#


#Classificar lista alfanumericamente

#Objetos de lista têm um sort()método que classificará a lista alfanumericamente, em ordem crescente, por padrão:

#Exemplo
#Classifique a lista em ordem alfabética:

thislist = ["orange", "mango", "kiwi", "pineaple", "banana"]

thislist.sort()
print(thislist)


#Exemplo
#Classifique a lista numericamente:

thislist = [100, 50, 65, 82, 23]

thislist.sort()
print(thislist)

#Personalizar função de classificação


#Você também pode personalizar sua própria função usando o argumento de palavra-chave .key = function

#A função retornará um número que será usado para classificar a lista (o menor número primeiro):

#Exemplo
#Classifique a lista com base na proximidade do número de 50:

def myfunction(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunction)
print(thislist)


#Classificação sem distinção entre maiúsculas e minúsculas

#Por padrão, o sort()método diferencia maiúsculas de minúsculas, resultando em todas as letras maiúsculas sendo classificadas antes das letras minúsculas:

#Exemplo

#A classificação com distinção entre maiúsculas e minúsculas pode gerar um resultado inesperado:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)



#Felizmente, podemos usar funções integradas como funções-chave ao classificar uma lista.

#Então, se você quiser uma função de classificação que não diferencia maiúsculas de minúsculas, use str.lower como uma função-chave:

#Exemplo

#Execute uma classificação da lista que não diferencia maiúsculas de minúsculas:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Ordem reversa
#E se você quiser inverter a ordem de uma lista, independentemente do alfabeto?

# reverse()método inverte a ordem de classificação atual dos elementos.

#Exemplo
#Inverta a ordem dos itens da lista:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)