#8 função alterando variavel local dentro da função e não a varialvel  global

a = 5
def muda_e_imprime():
    a = 7
    print("A dentro da função %d "% a)
print("a antes de mudar: %d" % a)
muda_e_imprime()#imprimindo a variavel local da função
print("a depois de mudar: %d"% a)

#mudando variavel global

a = 5
def muda_e_imprime():
    global a 
    a = 7
    print("A dentro da função: %d" % a)
print("a antes de mudar: %d" % a)
muda_e_imprime()
print("a depois de mudar: %d" % a)

'''OBS:USAR LETRAS MAIUSCULAS NAS VARIAVEIS GLOBAIS'''


