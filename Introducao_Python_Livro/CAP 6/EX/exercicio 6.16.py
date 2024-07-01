#Exercicio 6.16 pag 64

'''programa ordenação de metodo bolha'''
import time

l = [1, 2, 3, 4, 5]
fim = 5 #1  

while fim > 1:# 2 
    trocou = False#3
    x = 0#4
    print('Valor de x é: %d'% x)
    print('Valor de Trocou é %s' % trocou)
    
    while x < (fim - 1):#5
        
        if l[x] < l[x + 1]:#6
            print('{} Trocou com {}'.format(l[x], l[x + 1]))            
            trocou = True#7
            temp = l[x]#8
            l[x] = l[x + 1]
            l[x + 1] = temp
        x += 1
        time.sleep(1)

        
    print('Valor de x é: %d' % x)
    print('Valor de Trocou é: {}'.format(trocou))
    if not trocou:
        break
        fim -= 1
                    
        
for e in l:
    print(e)
    time.sleep(1)
        
