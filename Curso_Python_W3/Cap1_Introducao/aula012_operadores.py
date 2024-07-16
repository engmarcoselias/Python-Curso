#-----------------------------OPERADORES-----------------------------#

#Operadores Python
#Operadores são usados ​​para executar operações em variáveis ​​e valores.

#No exemplo abaixo, usamos o +operador para somar dois valores:

#Exemplo

print(10 + 5)

'''Python divide os operadores nos seguintes grupos:

Operadores aritméticos
Operadores de atribuição
Operadores de comparação
Operadores lógicos
Operadores de identidade
Operadores de associação
Operadores bit a bit
Python divide os operadores nos seguintes grupos:

Operadores aritméticos
Operadores de atribuição
Operadores de comparação
Operadores lógicos
Operadores de identidade
Operadores de associação
Operadores bit a bit
'''

# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	#divisão e sobra
# **   Exponentiation	x ** y	
# //  Floor division  x // y #divisão inteira

#Operadores de atribuição Python

#Operadores de atribuição são usados ​​para atribuir valores a variáveis:


# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3) x = 3

#Operadores de comparação Python

#Operadores de comparação são usados ​​para comparar dois valores:


# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y


# Operadores Lógicos Python

#Operadores lógicos são usados ​​para combinar instruções condicionais:


# and 	Returns True if both statements are true	x < 5 and  x < 10
	
# or	Returns True if one of the statements is true	x < 5 or x < 4	

#not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


#Operadores de identidade Python


#Operadores de identidade são usados ​​para comparar os objetos, não se eles são iguais, mas se eles são realmente o mesmo objeto, com o mesmo local de memória:


#is 	Returns True if both variables are the same object	x is y

#is not	Returns True if both variables are not the same object	x is not y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


#Operadores de Associação Python

#Operadores de associação são usados ​​para testar se uma sequência é apresentada em um objeto:


#in 	Returns True if a sequence with the specified value is present in the object	x in y
	
#not in	Returns True if a sequence with the specified value is not present in the object	x not in y

x = ["apple", "banana"]

print("banana" in x)


#Operadores Bitwise Python


#Operadores bit a bit são usados ​​para comparar números (binários):


# & 	AND	Sets each bit to 1 if both bits are 1	x & y	

# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	

# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	

# ~	NOT	Inverts all the bits	~x	

# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	

# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 



#operador precedente

#A precedência do operador descreve a ordem na qual as operações são executadas.

#Exemplo

#Parênteses têm a maior precedência, o que significa que as expressões dentro deles devem ser avaliadas primeiro:

print((6 + 3) - (6 + 3))

#A ordem de precedência é descrita na tabela abaixo, começando pela precedência mais alta no topo:

'''
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
'''

#Se dois operadores tiverem a mesma precedência, a expressão será avaliada da esquerda para a direita.

#Exemplo

#Adição +e subtração -têm a mesma precedência e, portanto, avaliamos a expressão da esquerda para a direita:

print(5 + 4 - 7 + 3)



