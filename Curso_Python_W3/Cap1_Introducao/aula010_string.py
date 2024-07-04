#--------------STRINGS EM PYTHON-----------#

#Exemplo
print("Hello")
print('Hello')

#Citações dentro de citações

#Você pode usar aspas dentro de uma string, desde que elas não correspondam às aspas ao redor da string:

#Exemplo
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#Atribuir String a uma Variável

#A atribuição de uma string a uma variável é feita com o nome da variável seguido por um sinal de igual e a string:

#xemplo
a = "Hello"
print(a)


#Strings multilinha

#Você pode atribuir uma string multilinha a uma variável usando três aspas:

#Exemplo
#Você pode usar três aspas duplas:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Ou três aspas simples:

#Exemplo
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Nota: no resultado, as quebras de linha são inseridas na mesma posição do código.

#------------------STRINGS SÃO MATRIZES-----------#

#omo muitas outras linguagens de programação populares, strings em Python são matrizes de bytes que representam caracteres Unicode.

#Entretanto, Python não tem um tipo de dado de caractere, um único caractere é simplesmente uma string com comprimento 1.

#colchetes podem ser usados ​​para acessar elementos da string.#

#Exemplo
#Pegue o caractere na posição 1 (lembre-se que o primeiro caractere tem a posição 0):

a = "Hello, World!"
print(a[1])


#Looping através de uma string

#Como strings são matrizes, podemos percorrer os caracteres em uma string com um forloop.

#Exemplo
#Faça um loop pelas letras da palavra "banana":

for x in "banana":
  print(x)



#Comprimento da String

#Para obter o comprimento de uma string, use a len()função.

#Exemplo
#
# A len()função retorna o comprimento de uma string:

a = "Hello, World!"
print(len(a))


#Verificar sequência de caracteres

#Para verificar se uma determinada frase ou caractere está presente em uma string, podemos usar a palavra-chave in.

#Exemplo
#Verifique se "free" está presente no texto a seguir:

txt = "The best things in life are free!"
print("free" in txt)
