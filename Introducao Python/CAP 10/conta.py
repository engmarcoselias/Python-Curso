#10.6classe conta

class Conta:
    def __init__(self, cliente, numero, saldo = 0):
        self.saldo = saldo
        self.cliente = cliente
        self.numero = numero
    def resumo(self):
        print("CC Número: %s Saldo: %10.2f" % (self.numero, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor