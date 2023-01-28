#9.19verificação se é diretorio ou arquivo

import os
import os.path

for a in os.listdir("."):
    if os.path.isdir(a):
        print("%s/"%a)
    elif os.path.isfile(a):
        print("%s"%a)

#para diretorio adicionamos uma barra no final