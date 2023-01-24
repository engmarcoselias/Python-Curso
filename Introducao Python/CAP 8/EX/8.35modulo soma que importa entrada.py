#importando modulo entrada(na hora de chamar o modulo preciso adicionar o prefixo do modulo e o nome da função EX: entrada.valida_inteiro)

'''import entrada

L= []

for x in range(10):
    L.append(entrada.valida_inteiro("Digite um numero: ", 0, 20))
print("Soma %d"% (x+(L)))'''

#com o from não preciso usar o prefixo do modulo para chamar a função
from entrada import valida_inteiro

L= []

for x in range(10):
    L.append(valida_inteiro("Digite um numero: ", 0, 20))
print("Soma %d"% ((L)))