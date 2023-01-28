#9.22obtenção das horas em python

import time

agora = time.time()
print(agora)

convert = time.ctime(agora)#horario UTC
print(convert)

local = time.localtime(agora)#trabalhando com horario do meu local
print(local)

local2 = time.gmtime(agora)#convert em uma tupla de 9 elementos
print(local2)

#9.23os dados da tupla podem ser acessados por nome

print("Ano: %s"% local2.tm_year)

'''PARA TRABALHAR COM DATA E HORA NOS PROGRAMAS 
CONSULTAR OS MODULOS TIME, DATETIME, CALENDAR E LOCALE'''

