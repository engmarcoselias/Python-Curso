#classe nome

class Nome:
    def __init__(self,nome):
        if nome == Nome or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return "<Classe{3} en 0x{0:x} Nome: {1} Chave: {2}>" .format (id(self),self.nome, self.chave, type(self).__name__)
    def __eq__(self, outro):
        print("__eq__Chamado")
        return self.nome == outro.nome
    def __lt__(self,outro):
        print("__lt__Chamado")
        return self.nome < outro.nome
