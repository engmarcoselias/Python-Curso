#-------------------LISTAS--------------------------------#

mylist = ["apple","banana", "herry"]

#Lista

#Listas são usadas para armazenar vários itens em uma única variável.

#Listas são um dos quatro tipos de dados internos do Python usados ​​para armazenar coleções de dados; os outros três são Tuple , Set e Dictionary , todos com qualidades e usos diferentes.

#As listas são criadas usando colchetes:

#lista de itens

#Os itens da lista são ordenados, alteráveis ​​e permitem valores duplicados.

#Os itens da lista são indexados, o primeiro item tem índice [0], o segundo item tem índice [1], etc.

#Ordenado

#Quando dizemos que as listas são ordenadas, isso significa que os itens têm uma ordem definida e essa ordem não mudará.

#Se você adicionar novos itens a uma lista, os novos itens serão colocados no final da lista:::Observação: existem alguns métodos de lista que alteram a ordem, mas, em geral, a ordem dos itens não muda.

#Mutável

#A lista é mutável, o que significa que podemos alterar, adicionar e remover itens de uma lista depois que ela foi criada.

#Permitir Duplicatas

#Como as listas são indexadas, elas podem ter itens com o mesmo valor:

#Exemplo
#Listas permitem valores duplicados:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#Comprimento da lista

#Para determinar quantos itens uma lista possui, use a len()função:

#Exemplo

#Imprima o número de itens na lista:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Itens da lista - Tipos de dados

#Os itens da lista podem ser de qualquer tipo de dados:

#Exemplo
#Tipos de dados string, int e booleanos:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Uma lista pode conter diferentes tipos de dados:

#Exemplo

#Uma lista com strings, inteiros e valores booleanos:

list1 = ["abc", 34, True, 40, "male"]


#tipo()

#Da perspectiva do Python, listas são definidas como objetos com o tipo de dados 'lista':

#<class 'list'>

#Exemplo

#Qual é o tipo de dado de uma lista?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#O construtor list()

#Também é possível usar o construtor list() ao criar uma nova lista.

#Exemplo

#Usando o list()construtor para fazer uma lista:

thislist = list(("apple", "banana", "cherry")) # obeserve os colchetes duplos
print(thislist)


#Coleções Python (Arrays)

#Existem quatro tipos de dados de coleção na linguagem de programação Python:

#Lista é uma coleção que é ordenada e mutável. Permite membros duplicados.

#Tuple é uma coleção que é ordenada e imutável. Permite membros duplicados.

#Set é uma coleção que não é ordenada, imutável* e não indexada. Nenhum membro duplicado.

#Dicionário é uma coleção que é ordenada** e mutável. Sem membros duplicados.
'''
* Os itens do conjunto são inalteráveis, mas você pode remover e/ou adicionar itens quando quiser.

**A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e anteriores, os dicionários são desordenados .


Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo. Escolher o tipo certo para um conjunto de dados específico pode significar retenção de significado e pode significar aumento de eficiência ou segurança.
'''