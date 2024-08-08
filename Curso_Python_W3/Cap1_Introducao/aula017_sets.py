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