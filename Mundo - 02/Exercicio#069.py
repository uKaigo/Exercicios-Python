p18 = h = mm20 = 0
while True:
    print('-' * 25)
    print(f'{"Cadastre uma pessoa":^25}')
    print('-' * 25)
    years = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).upper()[0]
    print('-' * 25)

    if years > 18:
        p18 += 1
    if sex == 'M':
        h += 1
    if sex == 'F' and years < 20:
        mm20 += 1

    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continar? [S/N] ')).upper().strip()[0]
    if conti == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {p18}\nAo todo temos {h} homens cadastrados\nE temos {mm20} mulheres com '
      f'menos de 20 anos')

