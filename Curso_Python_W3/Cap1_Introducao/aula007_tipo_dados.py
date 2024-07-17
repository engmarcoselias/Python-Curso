#----------------------------TIPO DE DOS E PYTHON----------------------------

'''Tipos de dados integradosNa programação, o tipo de dados é um conceito importante.
Variávei podem armazenar dados de diferentes tipos, e diferentes tipos podem fazer coisas diferentes.
Python tem os seguintes tipos de dados integrados por padrão, nestas categorias:'''



#Tipo de texto:	str
#Tipos numéricos:	int, float, complex
#Tipos de sequência:	list, tuple, range
#Tipo de mapeamento:	dict
#Tipos de conjunto:	set,frozenset
#Tipo booleano:	bool
#Tipos binários:	bytes, bytearray, memoryview
#Nenhum Tipo:	NoneType

#Obtendo o tipo de dados
#Você pode obter o tipo de dados de qualquer objeto usando a type()função:

#EX:

#Imprima o tipo de dados da variável x:

x = 5
print(type(x))

#Configurando o tipo de dados
#Em Python, o tipo de dado é definido quando você atribui um valor a uma variável:

#EX:
x = "Hello World"	                            #str	
x = 20	                                        #int	
x = 20.5	                                    #float	
x = 1j	                                        #complex	
x = ["apple", "banana", "cherry"]	            #list	
x = ("apple", "banana", "cherry")	            #tuple	
x = range(6)	                                #range	
x = {"name" : "John", "age" : 36}	            #dict	
x = {"apple", "banana", "cherry"}	            #set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                                    #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview	
x = None	                                    #NoneType




#Definindo o tipo de dados específico
#Se você quiser especificar o tipo de dados, poderá usar as seguintes funções construtoras:

#EX:
x = str("Hello World")	                        #str	
x = int(20)	                                    #int	
x = float(20.5)	                                #float	
x = complex(1j)	                                #complex	
x = list(("apple", "banana", "cherry"))	        #list	
x = tuple(("apple", "banana", "cherry"))	    #tuple	
x = range(6)	                                #range	
x = dict(name="John", age=36)	                #dict	
x = set(("apple", "banana", "cherry"))	        #set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	                                    #bool	
x = bytes(5)	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview	

#EX

a = list(("jose", "maria", "judas"))    
b = tuple([23, 25, 67])
c = dict(name="john", age=23)
print(type(a))                              #<class 'list'>
print(type(b))                              #<class 'tuple'>                              
print(type(c))                              #<class 'dict'>
print(a)                                    #['jose', 'maria', 'judas']
print(b)                                    #(23, 25, 67)
print(c)                                    #{'name': 'john', 'age': 23}
