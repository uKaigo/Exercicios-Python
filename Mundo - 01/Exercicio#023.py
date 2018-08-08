num = int(input('Insira um número: '))
# Utilizando STRING
print('\nStr:')
num = str(num)
print('Informações do número {:4}'.format(num))
print('Milhar: {}'.format(num[0]))
print('Centena: {}'.format(num[1]))
print('Dezena: {}'.format(num[2]))
print('Unidade: {}'.format(num[3]))

#Utilizando INT
print('\nInt:')
num = int(num)
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print('Milhar: ', m)
print('Centena: ', c)
print('Dezena: ', d)
print('Unidade: ', u)