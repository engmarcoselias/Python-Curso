'''Classe e Objeto--Propeiedades'''

#Criando uma classe com contrutor, adicionando atributos 
class Pessoa:
    def __init__(self, nome, idade, ativo):
        self.nome = nome
        self.idade = idade
        self.__ativo = ativo #atributo definido com  privado

#Declarando méthodos(define o corportamento de uma classse)
    
    def desativar(self):#definindo um méthodo
        self.__ativo = False #atributo definido com  privado
        print("A pessoa foi desativada com sucesso")

#usando propriedades para obter e enviar dados aos atributos privados de uma classe

    @property
    def ativo(self):
        return self.__ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo


#Instanciando objeto
a1 = Pessoa("marcos", 32,True)
#chamando o methodo
a1.desativar()
#printando com propriedades
print(a1.ativo)
