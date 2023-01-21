#8.23função retangulo parametros obrigatorios e opcionais

def retangulo(largura,altura,caractere = "*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

retangulo(10,20)
#chamando a função nomeando os argumentos


retangulo(altura=30, caractere="-",largura=30)

'''OBS: Quando especifiamos o parametro por nome devemos especificar todos com nome'''

