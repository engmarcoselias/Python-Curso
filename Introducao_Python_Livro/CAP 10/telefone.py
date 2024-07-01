#10.19classe telefone

class Telefone:
    def __init__(self,numero, tipo = None):
        self.numero = numero
        self.tipo = tipo
    def __str__(self):
        if self.tipo != None:
            tipo = self.tipo
        else:
            tipo = ""
        return "{0} {1}".format(self.numero, tipo)
    def __eq__(self, outro):
        return self.numero == outro.numero and (self.tipo == outro.tipo) or (self.tipo == None or outro.tipo == None)
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Número não pode sem None ou em branco")
        self.__numero = valor