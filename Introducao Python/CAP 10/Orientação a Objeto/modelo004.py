'''Classe e Objeto--ENCAPSULAMENTO'''

#========================================================================================================================================================
#Basicamente, o encapsulamento visa definir o que pode ou não ser acessado de forma externa da classe.
#
#Existem três tipos de atributos de visibilidade nas linguagens orientadas a objetos, que são:
#
#Public: Atributos e métodos definidos como públicos poderão ser invocados, acessados e modificados através de qualquer lugar do projeto;
#Private: Atributos e métodos definidos como privados só poderão ser invocados, acessados e modificados somente por seu próprio objeto.
#Protected: Atributos e métodos definidos como protegidos só poderão ser invocados, acessados e modificados por classes que herdam de outras classes através do conceito de Herança, visto na última aula. Sendo assim, apenas classes “filhas” poderão acessar métodos e atributos protegidos.
#
#========================================================================================================================================================

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



#Instanciando objeto

a1 = Pessoa("marcos", 32,True)
#chamando o metodo
a1.desativar()
#mudando valor do atributo(o valor não foi mudado so atribui um valor novo o  a um novo atributo)
a1.ativo = True
print(a1.ativo)


