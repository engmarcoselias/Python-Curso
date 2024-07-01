#alteração de nome de arquivos

import os

#os.mkdir("novo")
#os.rename("novo","velho")#renomeia o diretorio
#os.rmdir("novo")
#os.rmdir("velho")#apaga o diretorio

#criando e fechando um arquivo
open("teste.py","w").close()
os.remove("teste.py")#apagando um arquivo