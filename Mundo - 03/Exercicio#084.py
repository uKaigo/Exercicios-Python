pessoas = []
ma = me = 0
while True:
    pessoa = []
    n = input('Nome: ')
    p = float(input('Peso: '))
    pessoa.append(n)
    pessoa.append(p)
    if not pessoas:
        ma = me = p
    else:
        if p > ma:
            ma = p
        elif p < me:
            me = p
    pessoas.append(pessoa[:])
    con = input('Quer continuar? [S/N] ')[0]
    if con in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {ma:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == ma:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi {me:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == me:
        print(f'[{p[0]}] ', end='')