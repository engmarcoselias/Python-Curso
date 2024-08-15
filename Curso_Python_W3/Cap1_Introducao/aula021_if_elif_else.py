#-------------------------CONDIÇOES--------------------------------#


#Condições Python e instruções If
#Python suporta as condições lógicas usuais da matemática:
'''
É igual a: a == b
Não é igual a: a != b
Menor que: a < b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b
Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops.'''


#Uma "instrução if" é escrita usando a palavra-chave if .

#ExemploObtenha seu próprio servidor Python
#Declaração If:

a = 33
b = 200
if b > a:
  print("b is greater than a")


#Elif
#A palavra-chave elif é a maneira do Python dizer "se as condições anteriores não forem verdadeiras, então tente esta condição".

#Exemplo
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#Else

#A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores.

#Exemplo
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#Se você tiver apenas uma instrução para executar, você pode colocá-la na mesma linha da instrução if.

#Exemplo
#Declaração if de uma linha:

if a > b: print("a is greater than b")

#Se você tiver apenas uma instrução para executar, uma para if e uma para else, você pode colocar tudo na mesma linha:

#Exemplo
#Declaração if else de uma linha:

a = 2
b = 330
print("A") if a > b else print("B")


'''Essa técnica é conhecida como Operadores Ternários ou Expressões Condicionais .'''

#Você também pode ter várias instruções else na mesma linha:

#Exemplo
#Declaração if else de uma linha, com 3 condições:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#A declaração de passe

#if As instruções não podem estar vazias, mas se por algum motivo você tiver uma ifinstrução sem conteúdo, insira-a passpara evitar erros.

#Exemplo
a = 33
b = 200

if b > a:
  pass