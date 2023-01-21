# exercicio 6.13 pg 60 pdf

'''Programa para ler as temperaturas salvas em uma lista achar a maior a menor e
a media'''

temperatura = [-30, -8, 0, 1, 2, 5, -2, -4]
maximo = temperatura[0]
minimo = temperatura[0]
media1 = 0

for valor in temperatura:
    media1 = media1 + valor
    if maximo < valor:
        maximo = valor
    elif minimo > valor:
        minimo = valor

        

print('A temperatura maxima é de {}ºC'.format(maximo))
print('A temperatura minima é de %dºC' %(minimo))
print('A media de temperatura é de {}ºC'.format(media1/ len(temperatura)))

    
        
    
    
