def pesquisa(lista,telefone):
    for x in lista:
        if x == telefone:
            return True
    return "Telefone Não cadastrado"


l= ["37220001","37220002","37220003","37220004"]

while True: 
    add = l.append(input("Digite  telefone para adicionar: "))
    print(l)

    p = str(input("Digite o numero para pesquisar: "))

    print(pesquisa(l,p))


