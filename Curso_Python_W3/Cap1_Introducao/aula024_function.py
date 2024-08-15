#-----------------------FUNCTION-----------------#

#Funções Python
#Uma função é um bloco de código que só é executado quando é chamado.

#Você pode passar dados, conhecidos como parâmetros, para uma função.

#Uma função pode retornar dados como resultado.

#Criando uma função
#Em Python, uma função é definida usando a palavra-chave def :

#Exemplo

def my_function():
  print("Hello from a function")

#Chamando uma função
#Para chamar uma função, use o nome da função seguido por parênteses:

#Exemplo
def my_function():
  print("Hello from a function")

my_function()

#Argumentos

#Informações podem ser passadas para funções como argumentos.

#Os argumentos são especificados após o nome da função, dentro dos parênteses. Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

#O exemplo a seguir tem uma função com um argumento (fname). Quando a função é chamada, passamos um primeiro nome, que é usado dentro da função para imprimir o nome completo:

#Exemplo

def my_function(fname):
  print(fname + "Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

'''Os argumentos são frequentemente abreviados para args na documentação do Python.'''

#Parâmetros ou argumentos?

#Os termos parâmetro e argumento podem ser usados ​​para a mesma coisa: informações que são passadas para uma função.
'''
Da perspectiva de uma função:

Um parâmetro é a variável listada dentro dos parênteses na definição da função.

Um argumento é o valor que é enviado para a função quando ela é chamada.
'''

#Número de argumentos

#Por padrão, uma função deve ser chamada com o número correto de argumentos. O que significa que se sua função espera 2 argumentos, você tem que chamar a função com 2 argumentos, nem mais, nem menos.

#Exemplo
#Esta função espera 2 argumentos e obtém 2 argumentos:

def my_function(fname, lname):
  print(fname + " "+ lname)

my_function("Emil", "Refnes")


#Argumentos arbitrários, *args

#Se você não sabe quantos argumentos serão passados ​​para sua função, adicione *antes do nome do parâmetro na definição da função.

#Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens adequadamente:

#Exemplo
#Se o número de argumentos for desconhecido, adicione um *antes do nome do parâmetro:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "linus")

'''Argumentos arbitrários são frequentemente abreviados para *args na documentação do Python.'''

#Argumentos de palavras-chave

#Você também pode enviar argumentos com a sintaxe chave = valor .

#Dessa forma, a ordem dos argumentos não importa.

#Exemplo
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

'''A frase Argumentos de Palavras-chave é frequentemente abreviada para kwargs na documentação do Python.'''

#Argumentos de palavras-chave arbitrárias, **kwargs

#Se você não sabe quantos argumentos de palavra-chave serão passados ​​para sua função, adicione dois asteriscos: **antes do nome do parâmetro na definição da função.

#Dessa forma, a função receberá um dicionário de argumentos e poderá acessar os itens adequadamente:

#Exemplo
#Se o número de argumentos de palavra-chave for desconhecido, adicione um double **antes do nome do parâmetro:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

'''Argumentos Kword arbitrários são frequentemente abreviados para **kwargs na documentação do Python.'''



#Valor do parâmetro padrão
#O exemplo a seguir mostra como usar um valor de parâmetro padrão.

#Se chamarmos a função sem argumento, ela usará o valor padrão:

#Exemplo

def my_function(country = "Norway"):
  print("i am from" + country)

my_function("Brasil")
my_function("Argentina")
my_function("Australia")
my_function()
my_function("USA")

#Passando uma lista como argumento

#Você pode enviar qualquer tipo de dado de argumento para uma função (string, número, lista, dicionário etc.), e ele será tratado como o mesmo tipo de dado dentro da função.
#Por exemplo, se você enviar uma Lista como argumento, ela ainda será uma Lista quando chegar à função:

#Exemplo

def my_function(food):
  for x in food:
    print(x)

fruits = ["maça", "banana", "abacaxi"]

my_function(fruits)



#####--------------------VALORES DE RETORNO-----------------------######



#Para permitir que uma função retorne um valor, use a return instrução:

#Exemplo

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#A declaração de passe

#functiondefinições não podem estar vazias, mas se por algum motivo você tiver uma functiondefinição sem conteúdo, insira-a na passdeclaração para evitar um erro.

#Exemplo
def myfunction():
  pass

#Argumentos somente posicionais

#Você pode especificar que uma função pode ter SOMENTE argumentos posicionais ou SOMENTE argumentos de palavras-chave.

#Para especificar que uma função pode ter apenas argumentos posicionais, adicione , / após os argumentos:

#Exemplo
def my_function(x, /):
  print(x)

my_function(3)

#Sem isso, , /você tem permissão para usar argumentos de palavras-chave, mesmo que a função espere argumentos posicionais:

#Exemplo
def my_function(x):
  print(x)

my_function(x = 3)

#Mas ao adicionar, , /você receberá um erro se tentar enviar um argumento de palavra-chave:

#Exemplo
def my_function(x, /):
  print(x)

my_function(x = 3)


#Argumentos somente de palavras-chave

#Para especificar que uma função pode ter apenas argumentos de palavras-chave, adicione *, antes dos argumentos:

#Exemplo
def my_function(*, x):
  print(x)

my_function(x = 3)

#Sem isso, *, você tem permissão para usar argumentos posicionais, mesmo que a função espere argumentos de palavras-chave:

#Exemplo
def my_function(x):
  print(x)

my_function(3)

#Mas ao adicionar *, /você receberá um erro se tentar enviar um argumento posicional:

#Exemplo
def my_function(*, x):
  print(x)

my_function(3)

#Combine somente posicional e somente palavra-chave
#Você pode combinar os dois tipos de argumentos na mesma função.

#Qualquer argumento antes de é / ,somente posicional, e qualquer argumento depois de é *, somente palavra-chave.

#Exemplo
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


####--------------------RECURSÃO------------------------####


'''Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.

Recursão é um conceito matemático e de programação comum. Isso significa que uma função chama a si mesma. Isso tem o benefício de significar que você pode fazer um loop pelos dados para chegar a um resultado.

O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escorregar para escrever uma função que nunca termina, ou uma que usa quantidades excessivas de memória ou poder do processador. No entanto, quando escrita corretamente, a recursão pode ser uma abordagem muito eficiente e matematicamente elegante para a programação.

Neste exemplo, tri_recursion() é uma função que definimos para chamar a si mesma ("recurse"). Usamos a variável k como os dados, que decrementa ( -1 ) toda vez que recursionamos. A recursão termina quando a condição não é maior que 0 (ou seja, quando é 0).

Para um novo desenvolvedor, pode levar algum tempo para descobrir exatamente como isso funciona. A melhor maneira de descobrir é testando e modificando.'''

#Exemplo
#Exemplo de recursão

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
