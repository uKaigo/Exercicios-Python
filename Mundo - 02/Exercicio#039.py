from datetime import datetime
anoj = int(input('Digite o ano do seu nascimento: '))
anoa = datetime.today().year
idade = anoa - anoj

print('\nQuem nasceu em {} terá {} anos em {}!'.format(anoj, idade, anoa))
if idade == 18:
    print('Você terá que se alistar agora!')

elif idade < 18:
    sald = 18 - idade
    print('Você terá que se alistar em {} ano{}'.format(sald, 's' if sald > 1 else ''))
    print('Você se alistará em {}'.format(anoa + sald))

elif idade > 18:
    sald = idade - 18
    print('Você deveria ter se alistado á {} ano{}'.format(sald, 's' if sald > 1 else ''))
    print('Seu alistamento foi em {}'.format(anoa - sald))