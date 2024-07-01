'''Classe e objeto--Adicionado atributos a classe'''

#Criando uma classe com contrutor e adicionando atributos#

class Pessoa:
    def __init__(self, nome, idade):#constrtor __init__ (self, atributo 1, atributo 2)define as caracteristicas de uma classe

# Para definir os atributos de uma classe em seu construtor, basta passá-los como parâmetro, como podemos ver abaixo:
        self.nome = nome
        self.idade = idade

#Instanciando Objeto#

a1 = Pessoa("marcos", 32)
print(a1.nome, a1.idade)
