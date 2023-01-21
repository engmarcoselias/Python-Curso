# Exemplo 5.10

''' Programa para corrigir um teste multipla escolha de tres questoes
onde as respostas corretas sao ( b, a, d) nesta ordem'''


pontos = 0
questao = 1


while questao <= 0:

     resposta = input('Resposta da questão %d: '% questao)
     if questao == 1 and resposta == 'b':
          pontos = pontos + 1
     if questao == 2 and resposta == 'a':
          pontos = pontos + 1
     if questao == 3 and resposta == 'd':
          pontos = pontos + 1
     questao += 1
print('O aluno fes %d ponto(s)' % pontos)




