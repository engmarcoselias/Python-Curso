'''Classe e Objeto--metodos getter e setter'''

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

#=======================================================================================================================================================
#Caso precisemos acessar os atributos privados de uma classe, o Python oferece um mecanismo para construção de propriedades em uma classe e, dessa forma, melhorar a forma de encapsulamento dos atributos presentes. É comum que, quando queremos obter ou alterar os valores de um atributo, criamos métodos getters e setters para este atributo:
#=======================================================================================================================================================

#Definindo metodo getters e setters para atributos

    def get_ativo(self):
        return  self.__ativo
    def set_ativo(self, ativo):
        self.__ativo = ativo

#Instanciando objeto
a1 = Pessoa("marcos", 32,True)
#chamando o methodo
a1.desativar()
#printando o metodo getter
print(a1.get_ativo())


