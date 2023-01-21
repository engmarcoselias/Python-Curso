# Exemplo 6.17 e  6.18

# pagina 55 pdf

'''Adicionando elementos a lista com .append'''


l = []

l.append('a')

print(l)



l.append(['b', 'f']) # Utilizar o metodo adiciona a lista inteira em                       # 
                        # um so espaço da lista e nao ao final dela

                        
print(l)



l.extend(['c','d'])# Usando o metodo EXTEND o elemento adicionado será
                        # Acressentado ao final da lista em uma so posição
                        #nao adicionando uma lista dentro de outra com sua
                        #posição diferente de acordo com a sequencia.


print(l)
print(l[0], l[1], l[2], l[3])

