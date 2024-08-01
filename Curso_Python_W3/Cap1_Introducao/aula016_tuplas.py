#------------------TUPLAS-----------#


#Tupla
#Tuplas são usadas para armazenar vários itens em uma única variável.

#Tupla é um dos quatro tipos de dados internos do Python usados ​​para armazenar coleções de dados; os outros três são Lista , Conjunto e Dicionário , todos com qualidades e usos diferentes.

#Uma tupla é uma coleção ordenada e imutável .

#Tuplas são escritas com colchetes.

#Exemplo
#Criar uma Tupla:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuplas são imutáveis, o que significa que você não pode alterar, adicionar ou remover itens depois que a tupla é criada.
#Mas há algumas soluções alternativas.


#Alterar valores de tupla

#Uma vez que uma tupla é criada, você não pode alterar seus valores. Tuplas são inalteráveis , ou imutáveis ​​como também são chamadas.

#Mas há uma solução alternativa. Você pode converter a tupla em uma lista, alterar a lista e converter a lista de volta em uma tupla.

#Exemplo
#Converta a tupla em uma lista para poder alterá-la:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Adicionar itens


#Como tuplas são imutáveis, elas não têm um método interno append(), mas existem outras maneiras de adicionar itens a uma tupla.

#1. Converter em uma lista : assim como na solução alternativa para alterar uma tupla, você pode convertê-la em uma lista, adicionar seus itens e convertê-la novamente em uma tupla.

#Exemplo
#Converta a tupla em uma lista, adicione "laranja" e converta-a novamente em uma tupla:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#2. Adicione tupla a uma tupla . Você tem permissão para adicionar tuplas a tuplas, então se você quiser adicionar um item, (ou muitos), crie uma nova tupla com o(s) item(ns), e adicione-a à tupla existente:

#Exemplo
#Crie uma nova tupla com o valor "laranja" e adicione essa tupla:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Remover itens

'''Observação: você não pode remover itens de uma tupla.'''

#Tuplas são imutáveis , então você não pode remover itens delas, mas você pode usar a mesma solução alternativa que usamos para alterar e adicionar itens de tupla:

#Exemplo
#Converta a tupla em uma lista, remova "apple" e converta-a novamente em uma tupla:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Ou você pode excluir a tupla completamente:

#Exemplo
#A delpalavra-chave pode excluir a tupla completamente:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Descompactando uma Tupla

#Quando criamos uma tupla, normalmente atribuímos valores a ela. Isso é chamado de "empacotamento" de uma tupla:

#Exemplo
#Empacotando uma tupla:

fruits = ("apple", "banana", "cherry")

#Mas, em Python, também podemos extrair os valores de volta para variáveis. Isso é chamado de "descompactação":

#Exemplo
#Descompactando uma tupla:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

'''Observação: o número de variáveis ​​deve corresponder ao número de valores na tupla; caso contrário, você deve usar um asterisco para coletar os valores restantes como uma lista.'''

#Usando o Asterisk*

#Se o número de variáveis ​​for menor que o número de valores, você pode adicionar um *ao nome da variável e os valores serão atribuídos à variável como uma lista:

#Exemplo
#Atribua o restante dos valores como uma lista chamada "vermelho":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Se o asterisco for adicionado a outro nome de variável que não o anterior, o Python atribuirá valores à variável até que o número de valores restantes corresponda ao número de variáveis ​​restantes.

#Exemplo
#Adicione uma lista de valores à variável "tropic":

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)