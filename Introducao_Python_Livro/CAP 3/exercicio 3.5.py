#Pagina 31 pdf exercicio 3.6 livro Operadores logicos
materia1 = float(input('Nota da materia 1 : '))
materia2 = float(input('Nota da materia 2 : '))
materia3 = float(input('Nota da materia 3 : '))
resultado = materia1 > 7 and materia2 > 7 and materia3 > 7

if resultado == True:
    print('Aprovado')
else:
    print('Reprovado')
