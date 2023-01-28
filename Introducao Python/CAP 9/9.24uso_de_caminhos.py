#9.24uso de caminhos

import os.path

caminho = "i/j/k"
print(os.path.abspath(caminho))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))
print(os.path.split(caminho))
print(os.path.splitext(caminho))
print(os.path.splitdrive(caminho))
