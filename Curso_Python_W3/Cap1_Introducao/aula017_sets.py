#------------------------SETS---------------#


#Conjuntos(SETS) Python

myset = {"apple", "banana", "cherry"}

#Definição

#Conjuntos são usados ​​para armazenar vários itens em uma única variável.

#Conjunto é um dos quatro tipos de dados internos do Python usados ​​para armazenar coleções de dados; os outros três são Lista , Tupla e Dicionário , todos com qualidades e usos diferentes.

#Um conjunto é uma coleção que não é ordenada , imutável* e não indexada .

'''* Observação: os itens do conjunto são inalteráveis, mas você pode remover itens e adicionar novos.'''


#Os conjuntos são escritos com chaves.

#Exemplo
#Criar um conjunto:

thisset = {"apple", "banana", "cherry"}
print(thisset)

'''Observação: os conjuntos não são ordenados, então você não pode ter certeza em qual ordem os itens aparecerão.'''

#Itens definidos

#Os itens definidos não são ordenados, não podem ser alterados e não permitem valores duplicados.

#Não ordenado

#Não ordenado significa que os itens em um conjunto não têm uma ordem definida.

#Os itens do conjunto podem aparecer em uma ordem diferente cada vez que você os utiliza e não podem ser referenciados por índice ou chave.

#Imutável

#Os itens do conjunto são imutáveis, o que significa que não podemos alterá-los depois que o conjunto foi criado.

'''Depois que um conjunto é criado, você não pode alterar seus itens, mas pode remover itens e adicionar novos.'''

#Duplicatas não permitidas

#Os conjuntos não podem ter dois itens com o mesmo valor.

#Exemplo
#Valores duplicados serão ignorados:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

'''Nota: Os valores True e 1são considerados o mesmo valor em conjuntos e são tratados como duplicados:'''

#True e 1é considerado o mesmo valor:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

'''Nota: Os valores False e 0são considerados o mesmo valor em conjuntos e são tratados como duplicados:'''

#tipo()
#Da perspectiva do Python, conjuntos são definidos como objetos com o tipo de dados 'set':

#<class 'set'>

#O construtor set()
#Também é possível usar o construtor set() para criar um conjunto.

#Exemplo
#Usando o construtor set() para criar um conjunto:

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Acessar Itens de Conjunto

#Itens de acesso

#Você não pode acessar itens em um conjunto consultando um índice ou uma chave.

#Mas você pode percorrer os itens do conjunto usando um for loop, ou perguntar se um valor especificado está presente em um conjunto, usando a inpalavra-chave.

#Exemplo
#Percorra o conjunto e imprima os valores:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  #Exemplo
#Verifique se "banana" está presente no conjunto:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Exemplo
#Verifique se "banana" NÃO está presente no conjunto:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#Adicionar itens
'''Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens'''

#Para adicionar um item a um conjunto, use o add() método.

#Exemplo

#Adicione um item a um conjunto usando o add() método:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Adicionar conjuntos
#Para adicionar itens de outro conjunto ao conjunto atual, use o update() método .

#Exemplo
#Adicione elementos de tropicalem thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Adicionar qualquer iterável

#O objeto no update()método não precisa ser um conjunto, pode ser qualquer objeto iterável (tuplas, listas, dicionários etc.).

#Exemplo
#Adicione elementos de uma lista a um conjunto:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


####Remover itens definidos###


#Remover item
#Para remover um item de um conjunto, use remove()o método ou discard().

#Exemplo
#Remova "banana" usando o remove() método:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

'''Observação: se o item a ser removido não existir, remove()será gerado um erro.'''


#Exemplo
#Remova "banana" usando o discard() método:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


'''Observação: se o item a ser removido não existir, NÃOdiscard() será gerado um erro.'''

#Você também pode usar o pop()método para remover um item, mas esse método removerá um item aleatório, então você não pode ter certeza de qual item será removido.

#O valor de retorno do pop()método é o item removido.

#Exemplo
#Remova um item aleatório usando o pop() método:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#Exemplo
#O clear() método esvazia o conjunto:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


#Exemplo
#A delpalavra-chave excluirá o conjunto completamente:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

