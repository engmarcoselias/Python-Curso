#------------------FOR---------------#


#Python for


#Um loop for é usado para iterar(repetir, faser novamente) sobre uma sequência (que pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string).

#Isso é menos parecido com a palavra -chave for em outras linguagens de programação e funciona mais como um método iterador, como encontrado em outras linguagens de programação orientadas a objetos.

#Com o loop for podemos executar um conjunto de instruções, uma vez para cada item em uma lista, tupla, conjunto etc.

#Exemplo
#Imprima cada fruta em uma lista de frutas:

frutas = ["maça", "banana", "abacaxi", "melão"]

for x in frutas:
    print(x)

#O loop for não requer uma variável de indexação definida previamente.

#Looping através de uma string

#Mesmo as strings sendo objetos iteráveis, elas contêm uma sequência de caracteres:

#Exemplo
#Faça um loop pelas letras da palavra "banana":

for x in "banana":
  print(x)

#A declaração break

#Com a instrução break podemos parar o loop antes que ele tenha percorrido todos os itens:

#Exemplo
#Sair do loop quando xfor "banana":

frutas = ["maça", "pera", "uva", "abacaxi"]

for x in frutas:
   print(x)
   if x == "banana":
      break
   
#A declaração continue
#Com a instrução continue podemos parar a iteração atual do loop e continuar com a próxima:

#Exemplo
#Não imprima banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#############################################################################
#---------------------------------RANGE-------------------------------------#

#A função range()

#Para percorrer um conjunto de código um número especificado de vezes, podemos usar a função range() ,
#A função range() retorna uma sequência de números, começando em 0 por padrão, incrementando em 1 (por padrão) e terminando em um número especificado.


#Exemplo
#Usando a função range():

for x in range(6):
   print(x)

'''Observe que range(6) não são os valores de 0 a 6, mas os valores de 0 a 5.

A função range() assume 0 como valor inicial por padrão, no entanto, é possível especificar o valor inicial adicionando um parâmetro: range(2, 6) , que significa valores de 2 a 6 (mas não incluindo 6):'''

#Exemplo
#Usando o parâmetro start:

for x in range(2, 6):
  print(x)

'''A função range() incrementa a sequência em 1 por padrão, porém é possível especificar o valor do incremento adicionando um terceiro parâmetro: range(2, 30, 3 ) :'''

for x in range(2,30,3):
   print(x)

#Else no loop For

#A elsepalavra-chave em um forloop especifica um bloco de código a ser executado quando o loop for concluído:

#Exemplo
#Imprima todos os números de 0 a 5 e exiba uma mensagem quando o loop terminar:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

'''Nota: O elsebloco NÃO será executado se o loop for interrompido por uma breakinstrução.'''

#Exemplo
#Quebre o loop quando xfor 3 e veja o que acontece com o elsebloco:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Loops aninhados
#Um loop aninhado é um loop dentro de um loop.

#O "loop interno" será executado uma vez para cada iteração do "loop externo":

#Exemplo
#Imprima cada adjetivo para cada fruta:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#A declaração de passe
#for Os loops não podem estar vazios, mas se por algum motivo você tiver um forloop sem conteúdo, insira-o na passinstrução para evitar obter um erro.

#Exemplo
for x in [0, 1, 2]:
  pass