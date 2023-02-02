#10.7conta com registro de operações e extrato

class Conta2:
    def __init__(self, cliente, numero, saldo = 0):
        self.saldo = 0
        self.cliente = cliente
        self.numero = numero
        self.operacao = []
        self.deposito(saldo)
    def resumo(self):
        print("CC N%s Saldo: %10.2f" % (self.numero, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacao.append(["SAQUE", valor])
    def deposito(self, valor):
        self.saldo += valor
        self.operacao.append(["DEPÓSITO", valor])
    def extrato(self):
        print("Extrato CC Nº %s\n" % self.numero)
        for o in self.operacao:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n   Saldo:%10.2f\n"% self.saldo)
