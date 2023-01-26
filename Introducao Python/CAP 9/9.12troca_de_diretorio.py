#troca de diretorio

import os
os.chdir("a")
print(os.getcwd())#mostra o diretorio atual
os.chdir("..")#funçãopara mudar diretorio atual
print(os.getcwd())
os.chdir("b")
print(os.getcwd())
os.chdir("../c")
print(os.getcwd())