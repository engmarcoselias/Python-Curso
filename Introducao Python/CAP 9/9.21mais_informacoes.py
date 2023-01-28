#9.21obtenção de mais informações sobre arquivo

import os
import os.path
import time
import sys

print("Tamanho: %s"%os.path.getsize("entrada.txt"))
print("Criado: %s"%time.ctime(os.path.getctime("entrada.txt")) )#getctime retorna data e hora de criação
print("Modificado: %s"%time.ctime(os.path.getmtime("entrada.txt")))#getmtime modificação
print("Acessado: %s"%time.ctime(os.path.getatime("entrada.txt")))#getatime de acesso

''' OBS: os valore retornados pelas funções get são em segundos e 
    devem ser transformados em string pelo ctime'''