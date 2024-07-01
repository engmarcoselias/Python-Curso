# Exercicio 5.6 e 5.7

''' O intuito do exemplo era que o usuario digitasse um numero e programa
mostrase a sua tabuada foi modificado para ficar mais automatica e com
opção de escolha (referente ao exercicio 5.6 e 5.7 pdf)'''


y = int(input('Escolha a tabuada de qual numero: '))
fim = y * 10

x = 0
h = 0
while x <= fim:    
    print('{} X {} = {}'.format(y, h, x)) 
    x = x + y
    h = h + 1
    
