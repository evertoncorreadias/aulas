# leitura de milhar e separar
nome=int(input('digite uma milhar'))
u= nome//1 %10
d=nome//10%10
c=nome//100%10
m=nome//1000%10
print('milhar {}'.format(m))
print('centena{} '.format(c))
print('desena {}'.format(d))
print('unidade{}'.format(u))
