#--------------------WHILE------------------#

#Python Loops
#Python has two primitive loop commands:
'''
while loops
for loops
'''

#O loop while
#Com o loop while podemos executar um conjunto de instruções desde que uma condição seja verdadeira.

i = 1 

while 1 < 6:
    print(i)
    i += 1

'''Nota: lembre-se de incrementar i, caso contrário o loop continuará para sempre.

O loop while requer que as variáveis ​​relevantes estejam prontas. Neste exemplo, precisamos definir uma variável de indexação, i , que definimos como 1.'''


#A declaração break
#Com a instrução break podemos parar o loop mesmo se a condição while for verdadeira:

#Exemplo
#Saia do loop quando i for 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#A declaração continue
#Com a instrução continue podemos parar a iteração atual e continuar com a próxima:

#Exemplo
#Continue para a próxima iteração se i for 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#A declaração else
#Com a instrução else podemos executar um bloco de código uma vez quando a condição não for mais verdadeira:

#Exemplo
#Imprima uma mensagem quando a condição for falsa:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")