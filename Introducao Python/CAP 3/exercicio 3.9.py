#exercicio 3.9 conversão de entrada de dados pg 37 pdf
dia = float(input('Digites a quantidade de dias: '))
horas = float(input('Digite a quantidade de horas: '))
minutos = float(input('Digite a quantidade de minutos: '))
segundos = float(input('Digite a quantidades de segundos: '))
total = (dia*86400)+(horas*3600)+(minutos*60)+(segundos*1)# convertendo tudo para segundos
print('O valor em Dias é %d  as horas são %.02d:%.02d:%.02d e o total em segundos é %.2f.'% (dia, horas, minutos, segundos, total))
