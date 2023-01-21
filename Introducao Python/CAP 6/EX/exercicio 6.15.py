#Exercicio 6.15 pag 63

'''programa ordenação de metodo bolha'''
import time

l = [3, 3, 1, 5, 4]
fim = 5 #1  atribui valor 5 a variavel fim

while fim > 1:# 2  # enquanto o valor de fim for maior que 1 o loop continua
    trocou = False#3
    x = 0#4 # atribui valor  0 a variavel x
    print('Valor de x é: %d'% x)
    print('Valor de Trocou é %s' % trocou)
    
    while x < (fim - 1):#5 O loop continua enquanto o valor de x for menor que a variavel fim - 1
        
        if l[x] > l[x + 1]:#6 se a lista com indece x for maior que lista com indice x + 1 o if é executado
            print('{} Trocou com {}'.format(l[x], l[x + 1]))            
            trocou = True#7 
            temp = l[x]#8 a variavel (temp) passa a ter o valor do indice (x) da lista [l]
            l[x] = l[x + 1] # a posição (x) da lista l passa a ter o valor da posição  (x + 1) da lista [l]
            l[x + 1] = temp # a posição (x + 1) da lista [l] passa a ter o valor da variavel (temp)
        x += 1 # apos a execução do IF ou não da um acrescimo de 1 a variavel (x)
        time.sleep(1) # da um tempo de 1 segundo no print

        
    print('Valor de x é: %d' % x)
    print('Valor de Trocou é: {}'.format(trocou))
    if not trocou: # se trocou for falso pausar o loop de while x < fim - 1
        break
        fim -= 1 # decrementa 1 na variavel fime  voltar no primeiro loop e verificar se as condiçoes acontecem
                    
        
for e in l:
    print(e)
    time.sleep(1)
        
