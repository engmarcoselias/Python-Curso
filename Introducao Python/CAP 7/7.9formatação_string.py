#formatação utilizando metodo format

a = "{0} {1}".format("Alô","Mundo")
print(a)

#limitar tamanho de impressão dos parametros

a1 = "{0:10} {1}".format("123","456")
print(a1)

#espaços a esquerda ou direita

#a esquerda
a1 = "x{0:<10}x".format("123")
print(a1)

#a direita
a1 = "x{0:>10}x".format("123")
print(a1)

#centralizar
a1 = "x{0:^10}x".format("123")
print(a1)

#mascaras com elemento de lista

'''l1 = "{0[1]} {0[2]}".format(["123","456"])#não funcionou
print(l1)'''


#mascaras com elementos de dicionario

d2= "{0[nome]} {0[telefone]}".format({"telefone": 572,"nome":"Maria"})
print(d2)

#formatação de numeros

#7.36zeroa a esquerda
n1 ="{0:05}".format(5)
print(n1)

#7.37preenchimento com outro caracter
n2 = "{0:*=7}".format(31)
print(n2)

#alinhamento
n3 = "{0:*^10}".format(123)
print(n3)

n3 = "{0:*<10}".format(123)
print(n3)

n3 = "{0:*>10}".format(123)
print(n3)

#usando virgula para solicitar agrupamento por milhar e ponto para indicar precisão de numeros

#separação de milhares
n4 = "{0:,}".format(75320)
print(n4)

n4 = "{0:,.3f}".format(75320)
print(n4)

#formatação de inteiros

n4 = "{0:b}".format(7532)#binario
print(n4)

n4 = "{0:c}".format(65)#caracter
print(n4)

n4 = "{0:o}".format(5678)#octal
print(n4)

n4 = "{0:x}".format(5678)#hexadecimal minusculo
print(n4)

n4 = "{0:X}".format(5678)#hexadecimal com letra maiuscula
print(n4)

#o formato d e o formato n

n6 = "{:d}".format(5678)
print(n6)

n6 = "{:n}".format(5678)
print(n6)

import locale
pt = locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")
print(pt)

n6 = "{:n}".format(5678)
print(n6)

#formatando numros decimais

n5 = "{:f}".format(1579.543)
print(n5)

#depois de selecionar região pt_BR.utf-8
n5 = "{:n}".format(1579.543)
print(n5)


#exponencial
n5 = "{:e}".format(15795435.5665)
print(n5)

#porcentagem
n5 = "{:5.2%}".format(0.05)#multiplica por 100
print(n5)




















