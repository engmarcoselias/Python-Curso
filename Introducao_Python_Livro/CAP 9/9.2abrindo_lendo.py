#abrindo lendo e fechando arquivo

arquivo = open("Numero.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()