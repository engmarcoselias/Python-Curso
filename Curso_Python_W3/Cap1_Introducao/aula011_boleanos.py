#--------------------------------BOOLEANS EM PYTHON------------------------#

#Valores Booleanos
#Na programação, muitas vezes você precisa saber se uma expressão é Trueou False.

#Você pode avaliar qualquer expressão em Python e obter uma de duas respostas, Trueou False.

#Quando você compara dois valores, a expressão é avaliada e o Python retorna a resposta booleana:

#Exemplo
print(10 > 9)
print(10 == 9)
print(10 < 9)


#Quando você executa uma condição em uma instrução if, Python retorna Trueor False:

#Exemplo
#Imprima uma mensagem com base na condição True: False

a = "Marcos"

b = "Fabio"

if a == "Marcos":
    print("O Nome está correto")
if b == "Fabio":
    print("O nome Fabio está correto")
else:
    print("Nenhum nome está correto")

#A maioria dos valores são verdadeiros

#Quase todo valor é avaliado Truese tem algum tipo de conteúdo.

#Qualquer string é True, exceto strings vazias.

#Qualquer número é True, exceto 0.

#Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.

#Exemplo

#O seguinte retornará True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Alguns valores são falsos

#Na verdade, não há muitos valores que avaliam para False, exceto valores vazios, como (), [], {}, "", o número 0e o valor None. E, claro, o valor Falseavalia para False.

#Exemplo

#O seguinte retornará False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Mais um valor, ou objeto neste caso, é avaliado como False, e isso se você tiver um objeto feito de uma classe com uma __len__função que retorna 0 ou False:

#Exemplo

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))


#Funções podem retornar um booleano
#Você pode criar funções que retornam um valor booleano:

#Exemplo
#Imprima a resposta de uma função:

def myfunction():
    return True

print(myfunction())


#Você pode executar código com base na resposta booleana de uma função:

#Exemplo

#Imprima "SIM!" se a função retornar True, caso contrário imprima "NÃO!":

def myFunction():
    return True
if myFunction():
    print("YES")
else:
    print("NO")

#O Python também tem muitas funções integradas que retornam um valor booleano, como a isinstance() função , que pode ser usada para determinar se um objeto é de um determinado tipo de dados:

#Exemplo

#Verifique se um objeto é um inteiro ou não:

x = 200
print(isinstance(x, int))