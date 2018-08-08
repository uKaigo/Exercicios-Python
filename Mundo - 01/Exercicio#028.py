from random import randint
pc = randint(0, 5)
user = int(input('Pensei em um número de 0 - 5! Qual você pensa que é? '))
if user == pc:
    print('Acertou!!!')
else:
    print('Errou!!! Eu estava pensando no número {}!'.format(pc))