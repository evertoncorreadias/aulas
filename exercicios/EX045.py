from random import randint
from time import sleep
print('=====joquen po=====')
lista=('pedra','papel','tesoura')
computador=randint(0,2)

jogador=int(input('''digite 
[0]PEDRA
[1]PAPEL
[2]TESOURA 
digite sua escolha:'''))
print('JO')
sleep(1)
print('QUEM')
sleep(1)
print('PO')

print('=' *27)
print('voce escolheu {}'.format(lista[jogador]))
print('o computador escolheu {}'.format(lista[computador]))
print('=' *27)

if computador == 0:
    if jogador == 0:
        print('empatou')
    elif jogador ==1:
        print('voce perdeu')
    elif jogador == 2:
         print('voce ganhou')
    else:
        print('comando invalido')



if computador  == 1:
    if jogador == 0:
        print('voce perdeu')
    elif jogador == 1:
            print('empatou')
    elif jogador == 2:
            print('voce ganhou')
    else:
        print('comando invalido')



if computador == 2:
   if jogador == 0:
       print('voce ganhou')
   elif jogador == 1:
       print('voce perdeu')
   elif jogador == 2:
       print('empatou')
   else:
       print(' comando invalido')


