from datetime import datetime
y = int(input('Insira o ano de nascimento do atleta: '))
ya = datetime.today().year
i = ya - y

print('O atleta tem {} anos,'.format(i), end=' ')

clas = ''
if i <= 9:
    clas = 'MIRIM'
elif i <= 14:
    clas = 'INFANTIL'
elif i <= 19:
    clas = 'JUNIOR'
elif i <= 25:
    clas = 'SÊNIOR'
elif i > 25:
    clas = 'MASTER'

print('sua classificação é: {}.'.format(clas))
