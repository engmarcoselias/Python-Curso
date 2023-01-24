#8.34modulo entrada (entrada.py)

def valida_inteiro(mensagem, minimo, maximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= minimo and  v <= maximo:
                return v
            else:
                print("Digite um valor entre %d e %d"% (maximo, minimo))
        except:
            print("Você deve digitar um númwro inteiro")