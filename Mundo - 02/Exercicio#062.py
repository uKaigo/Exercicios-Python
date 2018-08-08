pt = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
num = 10
term = 1
contt = 10
while term > 0:
    print(pt, end=' ➜ ')
    num -= 1
    if num == 0:
        print('PAUSA')
        term = int(input('Deseja exibir mais quantos termos? '))
        contt += term
        num = term
    pt += ra
print('Progressão finalizada com {} termos!'.format(contt))
