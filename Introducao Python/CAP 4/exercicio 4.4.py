# Programa para ler um salario e calcular o valor do almento para salario
# inferior aumento de 10% para menores15%
# exercicio 4,4 pag 41 PDF

salario = float(input('Entre com o salario: R$ '))

if salario < 125000:
    salario = salario + (salario*15/100)
else:
    
    if salario >= 125000:
        salario = salario +(salario*10/100)
        
print('O salario com aumento é R$ %.2f' % salario)
