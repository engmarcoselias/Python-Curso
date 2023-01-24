#8.36gerando numeros aleatorios
import random

for x in range(10):
    print(random.randint(1, 100))#função radint recebe dois parametros inicio e fim dos numeros aleatorios

#8.38 numeros aleatorios entre 0 e 1

for x in range(10):
    print(random.random())

#8.39numeros aleatorios de ponto flutuante

for x in range(10):
    print(random.uniform(15,25))

#8.40seleção de amostras de uma lista aleatoriamente

print(random.sample(range(1,60),6))

#8.41ação de embaralha elementos de uma lista

a = list(range(1,11))
random.shuffle(a)
print(a)