#7.14centralizar texto (tamanho mais caracter de preenchimento)

s = "Tigre"
print("x"+s.center(10,".")+"x")

#7.15completar a string com espaço a direita e a esquerda

#esquerda
a = s.ljust(20)
print(a)

#direita
b = s.rjust(40)
print(b)

#7.15completar a string com espaço a direita e a esquerda

#esquerda
a = s.ljust(20,".")
print(a)

#direita
b = s.rjust(20,".")
print(b)

#7.18substituição de string(valor original, troca, repetição)

t = "um tigre, dois tigres, três tigres"
g = t.replace("tigre","gato")
print(g)

g1 = t.replace("tigre","gato",1)
print(g1)

#7.19remoção de espaços em branco

q = "     Olá      "
q1 = q.strip()
print(q1)

#remover a esquerda

q2 = q.lstrip()
print(q2)

#remover a direita

q3 = q.rstrip()
print(q3)

#passando parametro para strip

q4 = "/////....Ola...////"
q5 = q4.strip("/")
print(q5)

#7.21validação de string por conteudo

# se não estiver vazia e se for letras e numeros
a1 = "123ola"
r1 = a1.isalnum()
print(r1)
#se so conter letras
a2 = "ola"
r2 = a2.isalpha()
print(r2)
#se conter so numeros
a3 = "123"
r3 = a3.isdigit()
print(r3)

#7.24verificar se e maiusculo ou minusculo

b1 = "ABCD"
b2 = "abcd"

e1 = b1.isupper()#maiusculo
print(e1)

e1 = b1.islower()#minusculo
print(e1)

e2 = b2.isupper()#maiusculo
print(e2)

e2 = b2.islower()#minusculo
print(e2)

#7.26verificar se pode imprimir

g1 = "\n\t".isprintable()
print(g1)

g2 = "ola mundo".isprintable()
print(g2)


















