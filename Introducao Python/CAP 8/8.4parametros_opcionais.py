#8.17função para imprimir uma barra na tela

def barra():
    print("*"*40)
barra()


#8.18exibir uma barra com parametros opcionais

def barra(n = 40,caractere = "*"):
    print(caractere * n)
barra()

#passagem de parametros opcionais

barra(10)

barra(10,"-")

#função soma com parametros obrigatórios e opcionais(parametro opcional sempre o ultimo)

def soma(a,b,imprime = False):
    s = a + b
    if imprime:
        print(s)
    return s

soma(1,2,True)

soma(2,3)