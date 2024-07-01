#--------------------------------PYTHON CASTING--------------------------#

#Especificar um tipo de variável

#Pode haver momentos em que você queira especificar um tipo para uma variável. Isso pode ser feito com casting. Python é uma linguagem orientada a objetos e, como tal, usa classes para definir tipos de dados, incluindo seus tipos primitivos.

#A conversão em Python é, portanto, feita usando funções construtoras:

#int() - constrói um número inteiro a partir de um literal inteiro, um literal float (removendo todos os decimais) ou um literal de string (desde que a string represente um número inteiro)

#float() - constrói um número float a partir de um literal inteiro, um literal float ou um literal de string (desde que a string represente um float ou um inteiro)

#str() - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, literais inteiros e literais flutuantes


#Exemplo:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Exemplo


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Exemplo


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
