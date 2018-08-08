nu = int(input('Digite um número inteiro para tabuada: '))
msg = ''
print_ = ''
for c in range(1, 11):
    print_ += '{} X {:2} = {}\n'.format(nu, c, nu * c)
    msg = '{} X {:2} = {}'.format(nu, c, nu * c)

print('-' * len(msg))
print(print_, end='')
print('-' * len(msg))
