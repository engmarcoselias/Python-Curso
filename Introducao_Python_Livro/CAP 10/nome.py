#classe nome

class Nome:
    def __init__(self,nome):#__init__: método chamado para inicialização do objeto, logo após a sua construção;
        if nome == Nome or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")#A keyword raise é usada para gerar uma exceção.
                                                                    #Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):#__str__: método chamado pela função str() para obter o valor do objeto em forma de string;
        return self.nome
    def __repr__(self):#serve para representar um objeto como uma string
        return "<Classe{3} en 0x{0:x} Nome: {1} Chave: {2}>" .format (id(self),self.nome, self.chave, type(self).__name__)
    def __eq__(self, outro):# metodo de comparação
        print("__eq__Chamado")
        return self.nome == outro.nome
    def __lt__(self,outro):# metodo de comparação menor
        print("__lt__Chamado")
        return self.nome < outro.nome


