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



