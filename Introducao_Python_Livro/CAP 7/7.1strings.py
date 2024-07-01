#7.2uma string convertendo em lista
l = list("Alô Mundo")
print(l)

#7.2alterando valor da string

l[0] = "a"
print(l)

#7.2tranformando elementos da lista em uma string

l = "".join(l)
print(l)

#7.3verificação de uma string

nome = "João da Silva"
a = nome.startswith("João")
print(a)

b = nome.endswith("Silva")
print(b)

#7.4tranformando string em letras minusculos

m = nome.lower()
print(m)

#7.4tranformando string em letras maiusculas

m = nome.upper()
print(m)

#7.6verificar se a palavra pertence a string

p = "Silva" in nome
print(p)

#7.6verificar se a palavra não pertence a string

s = "Nós moramos logo ali"
l = "Nós" not in s
print(l)

#7.6contar a recorrencia de uma letra ou palavra em uma string

f = "uma arvore, duas arvores, três arvores derrubadas"
f1 = f.count("arvore")
f2 = f.count("a")
print(f1)
print(f2)

#7.3pesquisa de string(rfind pesquisa da direita para esquerda)

s1 = "Alô Mundo"
s2 = s1.find("ô")
print(s2)

s3 = s1.find("ok")
print(s3)#quando o valor não é encontrado retorna o valor -1


#7.11pesquisar limitando inicio e fim

d2 = "uma arvore, duas arvores, três arvores derrubadas"
d3 = d2.find("a",0,10)
print(d3)






