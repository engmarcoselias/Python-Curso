class pessoa:
    def __init__(self, valor):
        self.valor = valor
    @property
    def valor(self):
        self.__valor
        return print("ok")
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
        return print("Altera")
