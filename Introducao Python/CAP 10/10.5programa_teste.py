#10.5programa teste.py que importa a classe Cliente

from cliente import Cliente
from conta import Conta

joão = Cliente("joão","3322353232")
maria = Cliente("Maria","353535535")
c1 = Conta("João",123, 1200)


print("Nome: %s\nTelefone: %s"% (joão.nome,joão.telefone))
print(maria.nome)