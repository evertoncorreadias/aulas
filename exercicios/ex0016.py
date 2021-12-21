print('Calculo aluguel de veiculos')
n1=int(input('quantos dias ficou com o carro?'))
n2=float(input('quantos quilometros rodados'))
pago=(n1*60)+(n2*0.15)
print('o total a ser pagoé R${:.2f}'.format(pago))# os dois pontos ponto dois f (:.2f) formato dineiro