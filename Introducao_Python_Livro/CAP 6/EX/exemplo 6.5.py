# Exemplo 6.5

# pagina 52 PDF

'''programa para calcular a media de um aluno'''



notas = [6,7,5,8,9]     #1
soma = 0
x = 0


while x < 5:            #2
     soma += notas[x]   #3
     x += 1             #4
print('Média: %5.2f' % (soma/x))
