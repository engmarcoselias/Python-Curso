s = 0
numeros = 1

while True:
    v = int(input("Digite um número para somar ou 0 para sair: "))
    if v == 0:
        break
    numeros += 1
    s += v
print("A soma dos %d números digitados foi %d" %(numeros,s))