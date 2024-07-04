#-------------------------------STRINGS---------------------------#



#Looping através de uma string

#Como strings são matrizes, podemos percorrer os caracteres em uma string com um forloop.

#Exemplo

#Faça um loop pelas letras da palavra "banana":

for x in "banana":
  print(x)


#Comprimento da string

#Para obter o comprimento de uma string, use a função len().

#Exemplo

#A len()função retorna o comprimento de uma string:

a = "Hello, World!"
print(len(a))

#Verificar sequência de caracteres
#Para verificar se uma determinada frase ou caractere está presente em uma string, podemos usar a palavra-chave in.

#Exemplo

#Verifique se "free" está presente no texto a seguir:

txt = "The best things in life are free!"
print("free" in txt)

#Use-o em uma ifdeclaração:

#Exemplo

#Imprimir somente se "free" estiver presente:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Verifique se NÃO

#Para verificar se uma determinada frase ou caractere NÃO está presente em uma string, podemos usar a palavra-chave not in.

#Exemplo

#Verifique se "caro" NÃO está presente no texto a seguir:

txt = "The best things in life are free!"
print("expensive" not in txt)

#----------------------------------SLICING STRINGS(FATIAR STRING)----------------------------------#


#Fatiamento
#Você pode retornar um intervalo de caracteres usando a sintaxe de fatia.

#Especifique o índice inicial e o índice final, separados por dois pontos, para retornar uma parte da string.

#Exemplo

#Leve os caracteres da posição 2 para a posição 5 (não incluso):

b = "Hello, World!"
print(b[2:5])

#Fatiar desde o início
#Ao deixar de fora o índice inicial, o intervalo começará no primeiro caractere:

#Exemplo

#Obtenha os caracteres do início até a posição 5 (não incluída):

b = "Hello, World!"
print(b[:5])

#Fatiar até o fim
#Ao deixar de fora o índice final , o intervalo irá até o fim:

#Exemplo
#Pegue os caracteres da posição 2 até o final:

b = "Hello, World!"
print(b[2:])

#Indexação Negativa

#Use índices negativos para iniciar a fatia a partir do final da string:

#Exemplo

#Obtenha os personagens:

#De: "o" em "Mundo!" (posição -5)

#Para, mas não incluído: "d" em "Mundo!" (posição -2):

b = "Hello, World!"
print(b[-5:-2])

#-------------------------------------MODIFICAR STRINGS-------------------------------#

#O Python tem um conjunto de métodos integrados que você pode usar em strings.


#Maiúsculas

#ExemploObtenha seu próprio servidor Python
#O método upper() retorna a string em maiúsculas:

a = "Hello, World!"
print(a.upper())

#Minúsculas

#Exemplo
#O lower()método retorna a string em letras minúsculas:

a = "Hello, World!"
print(a.lower())


#Remover Espaço em Branco

#Espaço em branco é o espaço antes e/ou depois do texto real, e muitas vezes você deseja remover esse espaço.

#Exemplo

#O strip()método remove qualquer espaço em branco do início ou do fim:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!

#Substituir String

#Exemplo

#O replace()método substitui uma string por outra string:

a = "Hello, World!"
print(a.replace("H", "J"))

#Dividir String

#O split()método retorna uma lista onde o texto entre o separador especificado se torna os itens da lista.

#Exemplo

#O split()método divide a string em substrings se encontrar instâncias do separador:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']



#----------------------------CONCATENAÇÃO DE STRINGS----------------------------------#


#Concatenação de Strings

#Para concatenar ou combinar duas strings, você pode usar o operador +.

#Exemplo

#Mesclar variável acom variável bem variável c:

a = "Hello"
b = "World"
c = a + b
print(c)


#Exemplo

#Para adicionar um espaço entre eles, adicione " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)


#-----------------------------FORMATANDO STRINGS--------------------------------------------#


#Formato de sequência de caracteres

#Como aprendemos no capítulo Variáveis ​​Python, não podemos combinar strings e números desta forma:

#Exemplo
age = 36
txt = "My name is John, I am " + age
print(txt)

'''Traceback (most recent call last):
  File "demo_string_format_error.py", line 2, in <module>
    txt = "My name is John, I am " + age
TypeError: must be str, not int'''


#Mas podemos combinar strings e números usando f-strings ou o format()método !

#Strings F

#F-String foi introduzido no Python 3.6 e agora é a maneira preferida de formatar strings.

#Para especificar uma string como uma f-string, basta colocar um fna frente do literal da string e adicionar chaves {}como espaços reservados para variáveis ​​e outras operações.

#Exemplo

#Crie uma string f:

age = 36
txt = f"My name is John, I am {age}"
print(txt)


#Placeholders e Modificadores


#Um espaço reservado(placeholder) pode conter variáveis, operações, funções e modificadores para formatar o valor.

#Exemplo

#Adicione um espaço reservado para a variável price :

price = 59
txt = f"The price is {price} dollars"
print(txt)

#Um espaço reservado pode incluir um modificador para formatar o valor.

#Um modificador é incluído adicionando dois pontos :seguidos de um tipo de formatação legal, como .2fo que significa número de ponto fixo com 2 decimais:

#Exemplo

#Exibir o preço com 2 casas decimais:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Um espaço reservado pode conter código Python, como operações matemáticas:

#Exemplo

#Execute uma operação matemática no espaço reservado e retorne o resultado:

txt = f"The price is {20 * 59} dollars"
print(txt)


#------------------------CARACTER ESCAPE---------------------#

#Para inserir caracteres ilegais em uma string, use um caractere de escape.

#Um caractere de escape é uma barra invertida \seguida pelo caractere que você deseja inserir.

#Um exemplo de caractere ilegal são aspas duplas dentro de uma string cercada por aspas duplas:

#ExemploObtenha seu próprio servidor Python
#Você receberá um erro se usar aspas duplas dentro de uma string cercada por aspas duplas:

#Exemplo de erro
'''

txt = "We are the so-called "Vikings" from the north."

'''

#Para corrigir esse problema, use o caractere de escape \":

#Exemplo
#O caractere de escape permite que você use aspas duplas quando normalmente não seria permitido:

txt = "We are the so-called \"Vikings\" from the north."


#Caracteres de escape

#Outros caracteres de escape usados ​​em Python:

#Code	Result	Try it
#  \'	Single Quote	
#  \\	Backslash	
#  \n	New Line	
#  \r	Carriage Return	
#  \t	Tab	
#  \b	Backspace	
#  \f	Form Feed	
#  \ooo	Octal value	
#  \xhh	Hex value
