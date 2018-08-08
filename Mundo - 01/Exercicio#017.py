from math import hypot
co = float(input('Insira o cateto oposto: '))
ca = float(input('Insira o cateto adjecente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))