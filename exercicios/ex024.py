frase=('curso em video phyton')
print(frase.count("o")) #conta "O" da frase
print(len(frase)) #conta os caracteres da frase
print(frase.count('o'),0,13)# do zero ao 12 procura a letra "o"
print(frase.find('deo'))#onde começa o "d e o "
print(frase.find("android"))#procura a palavra "android",se nao encontrado =-1
print('curso 'in frase)#procura "curso" na frase
print(frase.replace("phyton",'android'))#troca frase do string
print(frase.upper())# transforma em maiuscula
print(frase.lower())# transforma em minuscula
print(frase.capitalize())#transforma somente a  primeira letra maiuscula
print(frase.title())# todas primeiras letras maiusculas
print(frase.strip())#remove espaços na string
print(frase.rstrip())#remove lado direito "vasio"da sring
print(frase.lstrip())#remove lado esquerdo"vasio" da sring
print(frase.split())#gera uma lista separada"subconjunto"
print('='.join (frase))#separaçao por "=" na frase



