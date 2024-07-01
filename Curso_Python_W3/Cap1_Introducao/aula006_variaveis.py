# variaveis são contêineres par armazenar valor de dados. Python não possui comando para declarar uma variável.

# Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.

#EX:

x1= 4
x2 = "Sally"
print(x1)
print(x2)

#Se você quiser especificar o tipo de dados de uma variavel, isso pode ser feito por conversão.

#EX:

x3 = str(3)
x4 = int(3)
x5= float(3)

print(x3)
print(x4)
print(x5)

#Você pode obter o tipo de dados de uma variavel com a type() função

#EX:

x6 = 5
y = "John"

print(type(x6))
print(type(y))

#Variaveis de string podem ser declaradas usando aspas simples ou duplas

#EX:

x7 = "John"
x8 = 'John'

#Os nomes das variaveis diferenciam maiúsculas e minúsculas

a = 4
A = "sally"

# Nomes das variaveis pode ter um nome curto(como x e y) ou um nome mais descritivo(idade, nome do carro, volume_total).
#Um nome de variável deve começar com uma letra ou o caractere sublinhado
#Um nome de variável não pode começar com um número
#Um nome de variável pode conter apenas caracteres alfanuméricos e sublinhados (Az, 0-9 e _)
#Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (idade, Idade e IDADE são três variáveis ​​diferentes)
#Um nome de variável não pode ser nenhuma das palavras-chave do Python

#EX:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Nomes de variaveis com mais de uma palava podem ser dificeis de ler . Existem várias écnicas que você pode usar para tornalos mais legiveis.

#CAMEL CASE

myVariableName = "John"

#PASCAL CASE

MyVariableName = "john"

#SNAKE CASE

my_variable_name = "john"



#Python permite atribuir valores a multiplas variaveis em uma linha

#EX:

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#Tambem e possivel atribuir o mesmo valor para múltiplas variaveis na mesma linha

#EX:

x=y=z = "Orange"
print(x)
print(y)
print(z)

#Se você tem uma coleção de valores em uma lista, tupla etc. Python permite que você extraia os valores em variáveis. Isso é chamado de unpacking .

#EX
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#VARIAVEIS DE SAIDA

#A função python print() é frequentemente usada para gerar variaveis.

x = "Python is aweasome"
print(x)

#Na print()função, você gera múltiplas variáveis, separadas por vírgula:

#EX
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Você também pode usar o +operador para gerar múltiplas variáveis:

#EX
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Observe o caractere de espaço depois de "Python "e "is ", sem eles o resultado seria "Pythonisawesome".

#Para números, o +caractere funciona como um operador matemático:

#EX
x = 5
y = 10
print(x + y)

#Na print()função, ao tentar combinar uma string e um número com o + operador, o Python apresentará um erro:

#EX
x = 5
y = "John"
print(x + y)

#A melhor maneira de gerar múltiplas variáveis ​​na print()função é separá-las com vírgulas, que suportam até mesmo diferentes tipos de dados:

#EX
x = 5
y = "John"
print(x, y)


##-------------------------VARIAVEIS GLOBAIS---------------------------#

#Variáveis ​​que são criadas fora de uma função (como em todos os exemplos nas páginas anteriores) são conhecidas como variáveis ​​globais.

#Variáveis ​​globais podem ser usadas por qualquer pessoa, tanto dentro quanto fora das funções.

#EX:

#Crie uma variável fora de uma função e use-a dentro da função

x_var = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Se você criar uma variável com o mesmo nome dentro de uma função, essa variável será local, e só poderá ser usada dentro da função. A variável global com o mesmo nome permanecerá como era, global e com o valor original.

#EX

#Crie uma variável dentro de uma função, com o mesmo nome da variável global

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




#--------------------------A PALAVRA CHAVE GLOBAL-----------------#

#Normalmente, quando você cria uma variável dentro de uma função, essa variável é local e só pode ser usada dentro dessa função.

#Para criar uma variável global dentro de uma função, você pode usar a globalpalavra-chave.

#Ex:

#Se você usar a global palavra-chave, a variável pertence ao escopo global:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#Além disso, use a globalpalavra-chave se quiser alterar uma variável global dentro de uma função.

#EX

#Para alterar o valor de uma variável global dentro de uma função, consulte a variável usando a globalpalavra-chave:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
