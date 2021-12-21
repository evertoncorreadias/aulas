from random import choice
print('=====joquen po=====')
jogador=str(input('escreva pedra papel ou tesoura ')).strip().lower()
lista=['pedra', 'papel' ,'tesoura']
computador=(choice(lista))

#PEDRA
if jogador == 'pedra' and computador == 'pedra':
    print('empatou')
elif jogador == 'pedra' and computador == 'papel':
    print('voce perdeu')
elif jogador == 'pedra' and computador =='tesoura':
    print('voce ganhou')
 # PAPEL
elif jogador == 'papel' and computador == 'pedra':
    print('voce ganhou')
elif jogador == 'papel' and computador == 'papel':
    print('empatou')
elif jogador == 'papel' and computador =='tesoura':
    print('voce perdeu')
 #TESOURA
elif jogador =='tesoura' and computador == 'pedra':
    print('voce perdeu')
elif jogador == 'tesoura' and computador == 'papel':
    print('voce ganhou')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('empatou')
else:
    print('jogada invalida')
