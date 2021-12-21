print('saiba se o numero digitado é par ou impar'.upper())

n1=(int(input('digite um numero'.upper())))
a= n1 % 2
if a==0:
    print('o numero digitado é par')
else:
    print ('o numero digitado é impar')