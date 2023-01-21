# exercicio 4.8
# Programa para ler dois numeros e que pergunta qual operação realizar +, -,* ,/.

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
operacao = str(input('Escolha uma operação +  -  *  / :  '))

if operacao == '+':
          resposta = n1 + n2
elif operacao == '-':
           resposta = n1 - n2
elif operacao == '*':
           resposta = n1 * n2
elif operacao == '/':
           resposta = n1 / n2
           
print('O resultado da sua operação é %2.f' % resposta)
           
