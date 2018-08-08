from datetime import date

atual = date.today().year
atin = 0
natin = 0
for c in range(1, 8):
    p = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - p
    if idade >= 21:
        atin += 1
    else:
        natin += 1
print('{} são maior de idade.\nE {} não são!'.format(atin, natin))
