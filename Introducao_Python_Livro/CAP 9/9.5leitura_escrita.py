#9.5filtragem exclusiva dos multiplos de quatro

multiplo4 = open("multiplo de 4.txt","w")
pares = open("pares.txt")

for l in pares.readlines():
    if int(l) % 4 == 0:
        multiplo4.write(l)
pares.cloe()
multiplo4.close()