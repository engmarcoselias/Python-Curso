'''#8.15validação sem usar uma função

while True:
    v = int(input("Digite um valor entre 0 e 5: "))
    if v < 0 or v > 5:
        print("Valor invalido.")
    else:
        break'''

#8.16validação usando função

def faixa_int(pergunta,minimo,maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print("Valor inválido. Digite um valor entre %d e %d" % (minimo, maximo))
        else:
            return v
faixa_int("Digite um valor: ",0,20)
