from time import strftime

year = int(input('Insira o ano atual, coloque 0 para o ano atual: '))

if year == 0:
    year = int(strftime('%Y'))

if year % 4 == 0:
    if year % 100 != 0:
        print('O ano {} é bixesto'.format(year))
    else:
        print('O ano {} não é bixesto'.format(year))
else:
    if year % 400 == 0:
        print('O ano {} não é bixesto'.format(year))
    else:
        print('O ano {} não é bixesto'.format(year))