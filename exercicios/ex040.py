from random import randint
print("adivinhe o numero de um a cinco")
numero=int(input('digite um numero '))
lista=randint(0,5)#faz o computador pensar em um numero aleatorio

if numero==lista:
    print('voce acertou!!!')
else:
    print('voce errou o numero è {}'.format(lista))