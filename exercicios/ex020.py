import random
print('='*30)
print('sorteio de seleçao de ordem')
print('='*30)
a=str(input('primeiro da seleçao'))
b=str(input('segundo da seleçao'))
c=str(input('terceiro da seleçao'))
d=str(input('quarto da seleçao'))
print('='*30)
lista=[a,b,c,d]
random.shuffle(lista)
print('a ordem de seleçao sera:')
print(lista)
print('='*30),print('fim')

