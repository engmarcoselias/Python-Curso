#9.1abrindo escrevendo e fechando arquivo

arquivo = open("Numero.txt","w")
for linha in range(1,101):
    arquivo.write("%d\n"%(linha))
arquivo.close