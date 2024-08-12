####---------DICTIONARY9DICIONARO)------####


#Copiar um dicionário

#Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2será apenas uma referência a dict1, e as alterações feitas em dict1serão feitas automaticamente também em dict2.

#Há maneiras de fazer uma cópia, uma delas é usar o método Dictionary integrado copy().

#Exemplo
#Faça uma cópia de um dicionário com o copy()método:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


#Outra maneira de fazer uma cópia é usar a função interna dict().

#Exemplo
#Faça uma cópia de um dicionário com a dict() função:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

###-----Dicionarios aninhados---###

#Dicionários Aninhados

#Um dicionário pode conter dicionários, isso é chamado de dicionários aninhados.

#Exemplo
#Crie um dicionário que contenha três dicionários:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Ou, se você quiser adicionar três dicionários em um novo dicionário:

#Exemplo
#Crie três dicionários e, em seguida, crie um dicionário que conterá os outros três dicionários:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Acessar itens em dicionários aninhados

#Para acessar itens de um dicionário aninhado, use o nome dos dicionários, começando pelo dicionário externo:

#Exemplo
#Imprima o nome da criança 2:

print(myfamily["child2"]["name"])


#Percorrer dicionários aninhados
#Você pode percorrer um dicionário usando o items()método como este:

#Exemplo
#Percorra as chaves e valores de todos os dicionários aninhados:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])


    ##############################
    #Metodos de dicionario#
    #https://www.w3schools.com/python/python_dictionaries_methods.asp
    ##############################