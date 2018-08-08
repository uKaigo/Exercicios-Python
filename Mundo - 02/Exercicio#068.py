from random import randint
vitorias = 0
print('=-' * 15)
print(f'{"Vamos jogar Pár ou Ímpar":^30}')

while True:
    print('=-' * 15)
    plval = int(input('Diga um valor: '))
    plesc = str(input('Pár ou Ímpar? [P/I] ')).upper()
    cpu = randint(0, 11)
    tot = plval + cpu
    if tot % 2 == 0:
        pi = 'PAR'
    else:
        pi = 'IMPAR'

    print('-' * 30)
    print(f'Você jogou {plval} e o computador {cpu}. Total de {tot}! Deu {pi}!')
    print('-' * 30)
    if plesc[0] == pi[0]:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        print('-' * 30)
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')
