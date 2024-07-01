'''Classe e Objeto--Adicionando méthodo a classe'''

#Criando uma classe com contrutor, adicionando atributos

class Pessoa:
    def __init__(self, nome, idade, ativo):
        self.nome = nome
        self.idade = idade
        self.ativo = ativo

#Declarando méthodos(define o corportamento de uma classse)
    
    #definindo um méthodo
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")



#Instanciando objeto

a1 = Pessoa("marcos", 32,True)
print(a1.nome, a1.idade,a1.ativo)

#chamando o metodo desativar 
a1.desativar()
print(a1.ativo)

