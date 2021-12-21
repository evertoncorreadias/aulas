print('o maior e o menor numero digitado')
a = int(input('digite um numero'))
b = int(input('digite o segundo numero'))
c = int(input('digite o terceiro numero'))

if b < a and b < c:
    menor = b
if a > b or a > c:
    menor = a
if c < a and c < b:
    menor = c

print('o menor numero digitado foi {}'.format(menor))

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('o maior numero digitado é {}'.format(maior))
