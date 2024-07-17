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
