#6.45criação de um dicionario

tabela = {  "alface":0.45,
            "Batata":1.20,
            "Tomate":2.30,
            "Feijão":1.50}
print(tabela)

#6.46adicionando chave
tabela["cebola"] = 2.56

print(tabela)

#6.48verificar se exixte uma chave

f = "cebola" in tabela
print(f)

#6.49obter lista de chaves

print(tabela.keys())

#6.49obter valores da tabela
print(tabela.values())

#6.51exclusão de uma associação do dicionario

del tabela["Tomate"]
print(tabela)

#dicioario com listas

estoque = {  "alface":[50,0.45],
            "Batata":[20,1.20],
            "Tomate":[60,2.30],
            "Feijão":[3,1.50]}
print(estoque)

#6.53exemplo dicionario como estoque usando metodo itens para retornar uma tupla

for chave,dados in estoque.items():
    print(chave,dados)