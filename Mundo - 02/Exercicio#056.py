yearoldsom = 0
m_old = 0
m_old_name = ''
mv = 0
for c in range(1, 5):
    pessoa = ' {}ª pessoa '.format(c)
    print(f'{pessoa:-^25}')
    name = str(input('Nome: ')).strip()
    yearold = int(input('Idade: '))
    sex = str(input('Sexo: (M/F) ')).strip()
    yearoldsom += yearold
    if sex in 'Mm' and yearold >= old:
        old = yearold
        old_name = name
    if sex in 'Ff' and yearold < 20:
        mv += 1
print('')
media = yearoldsom / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(old, m_old_name))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mv))