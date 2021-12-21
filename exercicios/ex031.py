d=int(input('distancia da viagem'))
print('sua viagem de {}km começou'.format(d))

if d <= 200:
    p = d * 0.5
else :
    p = d * 0.45
print('sua viagem ficou R${:1.2f}'.format(p)) #print no começo da linha para os dois valores da viagem

