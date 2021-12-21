
import random
a=str(input('primeiro aluno'))
b=str(input('segundo aluno'))
c=str(input('terceiro aluno'))
d=str(input('quarto aluno'))
lista=[a,b,c,d]
escolhido=random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))