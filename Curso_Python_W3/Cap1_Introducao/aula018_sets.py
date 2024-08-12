#-------------------CONTINUAÇÃO SET(CONJUNTOS)----------------------#


#Junte conjuntos
#Existem várias maneiras de juntar dois ou mais conjuntos em Python.

#Os union()métodos update()and unem todos os itens de ambos os conjuntos.

#O intersection()método mantém SOMENTE as duplicatas.

#O difference()método mantém os itens do primeiro conjunto que não estão nos outros conjuntos.

#O symmetric_difference()método mantém todos os itens EXCETO as duplicatas.

#União

#O union()método retorna um novo conjunto com todos os itens de ambos os conjuntos.

#Exemplo
#Junte set1 e set2 em um novo conjunto:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

'''Você pode usar o |operador em vez do union()método e obterá o mesmo resultado.'''

#Junte vários conjuntos

#Todos os métodos e operadores de junção podem ser usados ​​para unir vários conjuntos.

#Ao usar um método, basta adicionar mais conjuntos entre parênteses, separados por vírgulas:

#Exemplo

#Exemplo
#Junte vários conjuntos com o union()método:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Exemplo
#Junte vários conjuntos com o union()método:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Junte um conjunto e uma tupla

#O union()método permite que você junte um conjunto com outros tipos de dados, como listas ou tuplas.

#O resultado será um conjunto.

#Exemplo
#Junte um conjunto com uma tupla:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


'''Observação: o  | operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o  union()método.'''

#Atualizar
#O update()método insere todos os itens de um conjunto em outro.

#Isso update()altera o conjunto original e não retorna um novo conjunto.

#Exemplo
#O update()método insere os itens do conjunto2 no conjunto1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

'''Observação: ambos union()e update() excluirão quaisquer itens duplicados.'''

#Interseção
#Mantenha SOMENTE as duplicatas

#O intersection()método retornará um novo conjunto, que contém apenas os itens que estão presentes em ambos os conjuntos.

#Exemplo
#Junte set1 e set2, mas mantenha apenas as duplicatas:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Você pode usar o &operador em vez do intersection()método e obterá o mesmo resultado.

#Exemplo
#Use &para unir dois conjuntos:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)


'''Observação: o & operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o intersection()método.'''

#O intersection_update()método também manterá SOMENTE as duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto.

#Exemplo
#Mantenha os itens que existem em ambos set1, e set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

#Diferença

#O difference()método retornará um novo conjunto que conterá apenas os itens do primeiro conjunto que não estão presentes no outro conjunto.

#Exemplo
#Mantenha todos os itens do conjunto1 que não estão no conjunto2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Você pode usar o -operador em vez do difference()método e obterá o mesmo resultado.

#Exemplo
#Use -para unir dois conjuntos:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

'''Observação: o - operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o difference()método.'''


#O difference_update()método também manterá os itens do primeiro conjunto que não estão no outro conjunto, mas alterará o conjunto original em vez de retornar um novo conjunto.

#Exemplo
#Use o difference_update()método para manter os itens que não estão presentes em ambos os conjuntos:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#Diferenças Simétricas
#O symmetric_difference()método manterá apenas os elementos que NÃO estão presentes em ambos os conjuntos.

#Exemplo
#Mantenha os itens que não estão presentes em ambos os conjuntos:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#Você pode usar o ^operador em vez do symmetric_difference()método e obterá o mesmo resultado.

#Exemplo
#Use ^para unir dois conjuntos:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

'''bservação: o ^ operador só permite que você junte conjuntos com conjuntos, e não com outros tipos de dados, como você pode fazer com o symmetric_difference()método.'''


#O symmetric_difference_update()método também manterá tudo, exceto as duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto.

#Exemplo
#Use o symmetric_difference_update()método para manter os itens que não estão presentes em ambos os conjuntos:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

###################################
#-----Metodos de Conjunto---------#
#https://www.w3schools.com/python/python_sets_methods.asp
###################################


