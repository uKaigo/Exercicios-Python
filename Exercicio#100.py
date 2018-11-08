from time import sleep
from random import randint
numeros = list()


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(0, 10)
        numeros.append(n)
        sleep(0.3)
        print(n, end=' ', flush=True)
    print('PRONTO!')


def somapar():
    smp = 0
    for c in numeros:
        if c % 2 == 0:
            smp += c
    print(f'Somando os valores pares de {numeros}, temos {smp}')


sorteia()
somapar()
