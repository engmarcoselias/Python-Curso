#-----------DICTIONARY-------#



#Dicionarios


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Dicionário

#Dicionários são usados ​​para armazenar valores de dados em pares chave:valor.

#Um dicionário é uma coleção ordenada*, mutável e que não permite duplicatas.

#Os dicionários são escritos com chaves e têm chaves e valores:

#Exemplo
#Crie e imprima um dicionário:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


#Itens do dicionário
#Os itens do dicionário são ordenados, alteráveis ​​e não permitem duplicatas.

#Os itens do dicionário são apresentados em pares chave:valor e podem ser referenciados usando o nome da chave.

#Exemplo
#Imprima o valor "marca" do dicionário:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Ordenado ou não ordenado?

#A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e anteriores, os dicionários são desordenados .

#Quando dizemos que os dicionários são ordenados, isso significa que os itens têm uma ordem definida e essa ordem não mudará.

#Não ordenado significa que os itens não têm uma ordem definida; você não pode se referir a um item usando um índice.

#Mutável

#Os dicionários são mutáveis, o que significa que podemos alterar, adicionar ou remover itens depois que o dicionário for criado.

#Duplicatas não permitidas

#Os dicionários não podem ter dois itens com a mesma chave:

#Exemplo
#Valores duplicados substituirão os valores existentes:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#O construtor dict()

#Também é possível usar o construtor dict() para criar um dicionário.

#Exemplo
#Usando o método dict() para criar um dicionário:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#Acessando Itens

#Você pode acessar os itens de um dicionário consultando seu nome de chave, dentro de colchetes:

#Exemplo
#Obtenha o valor da chave "model":

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


#Existe também um método chamado get()que lhe dará o mesmo resultado:

#Exemplo
#Obtenha o valor da chave "model":

x = thisdict.get("model")


#Obter chaves
#O keys()método retornará uma lista de todas as chaves no dicionário.

#Exemplo
#Obtenha uma lista das chaves:

x = thisdict.keys()


'''A lista de chaves é uma visualização do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de chaves.'''

#Exemplo
#Adicione um novo item ao dicionário original e veja se a lista de chaves também é atualizada:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#Obter valores
#O values()método retornará uma lista de todos os valores no dicionário.

#Exemplo
#Obtenha uma lista dos valores:

x = thisdict.values()

#A lista de valores é uma visão do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de valores.

#Exemplo
#Faça uma alteração no dicionário original e veja se a lista de valores também é atualizada:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Exemplo
#Adicione um novo item ao dicionário original e veja se a lista de valores também é atualizada:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)

car["color"] = "red"

print(x)

#Obter itens

#O items()método retornará cada item em um dicionário, como tuplas em uma lista.

#Exemplo
#Obtenha uma lista dos pares chave:valor

x = thisdict.items()

'''A lista retornada é uma visualização dos itens do dicionário, o que significa que quaisquer alterações feitas no dicionário serão refletidas na lista de itens.'''


###Alterar itens do dicionário###


#Alterar valores

#Você pode alterar o valor de um item específico consultando seu nome de chave:

#Exemplo
#Altere o "ano" para 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Atualizar dicionário

#O update()método atualizará o dicionário com os itens do argumento fornecido.

#O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.Se o item não existir, o item será adicionado.

#Exemplo
#Atualize o "ano" do carro usando o update() método:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


###Adicionar itens de dicionário###

#Adicionando Itens

#Adicionar um item ao dicionário é feito usando uma nova chave de índice e atribuindo um valor a ela:

#Exemplo
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


###Remover itens do dicionário###


#Removendo Itens
#Existem vários métodos para remover itens de um dicionário:

#Exemplo
#O pop()método remove o item com o nome de chave especificado:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#Exemplo
#O popitem()método remove o último item inserido (em versões anteriores à 3.7, um item aleatório é removido):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#Exemplo
#A delpalavra-chave remove o item com o nome de chave especificado:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#Exemplo
#A delpalavra-chave também pode excluir o dicionário completamente:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

#Exemplo
#O clear()método esvazia o dicionário:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

###Loop através de um dicionário###


#Você pode percorrer um dicionário usando um forloop.

#Ao percorrer um dicionário, o valor de retorno são as chaves do dicionário, mas também existem métodos para retornar os valores .

#Exemplo
#Imprima todos os nomes de chaves no dicionário, um por um:

for x in thisdict:
  print(x)


#Exemplo
#Imprima todos os valores no dicionário, um por um:

for x in thisdict:
  print(thisdict[x])

#Exemplo
#Você também pode usar o values()método para retornar valores de um dicionário:

for x in thisdict.values():
  print(x)

#Exemplo
#Você pode usar o keys()método para retornar as chaves de um dicionário:

for x in thisdict.keys():
  print(x)


#Exemplo
#Faça um loop por chaves e valores usando o items()método:

for x, y in thisdict.items():
  print(x, y)
