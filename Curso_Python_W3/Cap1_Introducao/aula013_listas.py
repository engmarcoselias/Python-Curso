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


#=============================================================#

#--------------------------PYTHON ITENS DA LISTA DE ACESSO-------------------#

# Itens de acesso
#Os itens da lista são indexados e você pode acessá-los consultando o número do índice:

#Exemplo

#Imprima o segundo item da lista:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Indexação Negativa
#Indexação negativa significa começar do fim

# -1 refere-se ao último item, -2refere-se ao penúltimo item etc.

#Exemplo

#Imprima o último item da lista:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Faixa de índices
#Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo.

#Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.

#Exemplo
#Retorne o terceiro, quarto e quinto item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

'''Observação: a pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).

Lembre-se de que o primeiro item tem índice 0.'''



#Ao deixar de fora o valor inicial, o intervalo começará no primeiro item:

#Exemplo
#Este exemplo retorna os itens do início até "kiwi", mas NÃO incluindo:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Ao deixar de fora o valor final, o intervalo irá para o final da lista:

#Exemplo
#Este exemplo retorna os itens de "cherry" até o final:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Faixa de índices negativos
#Especifique índices negativos se quiser iniciar a pesquisa a partir do final da lista:

#Exemplo
#Este exemplo retorna os itens de "laranja" (-4) para, mas NÃO incluindo "manga" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#Verifique se o item existe
#Para determinar se um item especificado está presente em uma lista, use a inpalavra-chave:

#Exemplo
#Verifique se "apple" está presente na lista:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#=================================================================#

#----------------------ALTERAR ITENS DA LISTA---------------------#


#Alterar valor do item
#Para alterar o valor de um item específico, consulte o número do índice:

#Exemplo

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)



#Alterar um intervalo de valores de itens
#Para alterar o valor dos itens dentro de um intervalo específico, defina uma lista com os novos valores e consulte o intervalo de números de índice onde deseja inserir os novos valores:

#Exemplo
#Altere os valores "banana" e "cereja" pelos valores "groselha preta" e "melancia":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Se você inserir mais itens do que substituir, os novos itens serão inseridos onde você especificou, e os itens restantes serão movidos de acordo:

#Exemplo
#Altere o segundo valor substituindo-o por dois novos valores:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


'''Observação: o comprimento da lista mudará quando o número de itens inseridos não corresponder ao número de itens substituídos.'''

#Se você inserir menos itens do que substituir, os novos itens serão inseridos onde você especificou, e os itens restantes serão movidos de acordo:

#Exemplo
#Altere o segundo e o terceiro valor substituindo-os por um valor:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Inserir Itens
#Para inserir um novo item de lista, sem substituir nenhum dos valores existentes, podemos usar o insert()método .

#O insert()método insere um item no índice especificado:

#Exemplo
#Insira "melancia" como terceiro item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#==================================================#

#-------------------ADICIONAR ITENS A LISTA---------------------#

#Adicionar itens
#Para adicionar um item ao final da lista, use o método append() :

#ExemploObtenha seu próprio servidor Python
#Usando o append()método para anexar um item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Inserir Itens
#Para inserir um item de lista em um índice especificado, use o insert()método .

#O insert()método insere um item no índice especificado:

#Exemplo
#Insira um item como segunda posição:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Estender lista
#Para acrescentar elementos de outra lista à lista atual, use o extend()método .

#Exemplo
#Adicione os elementos tropicalde thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


'''Os elementos serão adicionados ao final da lista.'''

#Adicionar qualquer iterável
#O extend()método não precisa anexar listas , você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).

#Exemplo
#Adicione elementos de uma tupla a uma lista:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#=======================================================================#

#------------------------REMOVER ITENS DA LISTA-----------------------#


#Remover item especificado
#O remove()método remove o item especificado.

#Exemplo
#Remover "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Se houver mais de um item com o valor especificado, o remove()método remove a primeira ocorrência:

#Exemplo
#Remova a primeira ocorrência de "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remover índice especificado
#O pop()método remove o índice especificado.

#Exemplo
#Remova o segundo item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Se você não especificar o índice, o pop()método removerá o último item.

#Exemplo
#Remova o último item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#A del palavra-chave também remove o índice especificado:

#Exemplo
#Remova o primeiro item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#A del palavra-chave também pode excluir a lista completamente.

#Exemplo
#Apagar a lista inteira:

thislist = ["apple", "banana", "cherry"]
del thislist


#Limpar a lista
#O clear()método esvazia a lista.

#A lista ainda permanece, mas não tem conteúdo.

#Exemplo
#Limpar o conteúdo da lista:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)