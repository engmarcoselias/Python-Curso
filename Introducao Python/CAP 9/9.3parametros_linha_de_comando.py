#9.3impressão de parametros passados na linha de comando

import sys

print("Numero de parâmetros: %d"%len(sys.argv))
for n,p in enumerate(sys.argv):
    print("Parâmetro %d = %s"%(n,p))