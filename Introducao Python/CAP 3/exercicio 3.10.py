salario = float(input('Entre com o valor do salario R$ '))
porcento = float(input('Entre com o valor da porcentagem:  '))
aumento = salario*porcento/100
print('O valor do salario é R$ %.2f com um aumento de %.0f porcento passa a ser R$ %.2f.'%(salario, porcento, aumento+salario))
