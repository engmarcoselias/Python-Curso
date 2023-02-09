#Métodos de ordenação de comparação de uma classe


'''No entanto, podemos simplificar o processo com o total_orderingdescritor . Podemos definir qualquer um dos métodos de ordenação de comparação e o decorador fornece o restante dos métodos. A classe também deve fornecer um __eq__()método.'''

from functools import total_ordering

'''
__lt__(): método menor que
__le__(): Menor ou igual ao método
__gt__(): Método maior que
__ge__(): Maior ou igual ao método
__eq__(): Igual ao método
'''


@total_ordering

class pessoa:

    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    def __lt__(self, outra):
        return self.idade < outra
