from math import sin, tan, cos, radians
val = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(val))
cosseno = cos(radians(val))
tangente = tan(radians(val))
print('O número {0} tem o SENO de: {1:.2f}\n'
      'O número {0} tem o COSSENO de: {2:.2f}\n'
      'O número {0} tem o TANGENTE de: {3:.2f}'.format(val, seno, cosseno, tangente))