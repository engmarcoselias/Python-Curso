#==================CONTINUAÇÃO LISTAS========================#


#--------------------LISTAS DE COPIAS-------------------------#


#Copiar uma lista

#Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2será apenas uma referência a list1, e as alterações feitas em list1serão feitas automaticamente também em list2.

#Há maneiras de fazer uma cópia, uma delas é usar o método List integrado copy().

#Exemplo
#Faça uma cópia de uma lista com o copy()método:

thislist = ["aple", "banana","cherry"]
mylist = thislist.copy()
print(mylist)

#Outra maneira de fazer uma cópia é usar o método interno list().

#Exemplo
#Faça uma cópia de uma lista com o list()método:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


#Junte duas listas

#xistem várias maneiras de juntar ou concatenar duas ou mais listas em Python.

#Uma das maneiras mais fáceis é usar o + operador.

#Exemplo
#Junte-se a duas listas:

lista1 = ["a", "b", "c"]
lista2 = [1,2,3]

lista3 = lista1 + lista2
print(lista3)


#Outra maneira de unir duas listas é anexar todos os itens da lista2 na lista1, um por um:

#Exemplo
#Acrescente list2 em list1:

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

for x in lista2:
    lista1.append(x)

print(lista1)

#Ou você pode usar o extend() método, cujo objetivo é adicionar elementos de uma lista a outra:

lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

list.extend(lista2)
print(lista1)


#Métodos de lista

#O Python tem um conjunto de métodos integrados que você pode usarem listas.

'''
append()	Adds an element at the end of the list

clear()	Removes all the elements from the list

copy()	Returns a copy of the list

count()	Returns the number of elements 
with the specified value

extend()	Add the elements of a list (or any iterable), to the end of the current list

index()	Returns the index of the first 
element with the specified value

insert()	Adds an element at the specified position

pop()	Removes the element at the specified position

remove()	Removes the item with the specified value

reverse()	Reverses the order of the list

sort()	Sorts the list'''