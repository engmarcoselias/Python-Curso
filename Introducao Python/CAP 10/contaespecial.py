#10.11uso de herança para definir conta especial

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

class ContaEspecial(Conta2):
    def __init__(self, cliente, numero, saldo=0, limite = 0):
        Conta2.__init__(self, cliente, numero, saldo)# Quado se utiliza herança o metodo construtor da super classe deve ser chamado(Conta2__init__))
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacao.append(["SAQUE",valor])