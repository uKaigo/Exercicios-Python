from random import randint
from time import sleep
print('-=' * 10)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
player = int(input('Qual a sua jogada? '))
print('-=' * 10)
pc = randint(0, 2)
choices = ['Pedra', 'Papel', 'Tesoura', 'INVALIDO']
if player != 0 and player != 1 and player != 2:
    player = 3
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 10)
print('Computador jogou {}'.format(choices[pc]))
print('Jogador jogou {}'.format(choices[player]))
print('-=' * 10)
if pc == 0:
    if player == 0:
        print('Empate!')
    elif player == 1:
        print('Jogador VENCE!')
    elif player == 2:
        print('Computador VENCE!')
    else:
        print('\033[31m', 'Jogada Invalida!', '\033[m')

elif pc == 1:
    if player == 0:
        print('Computador VENCE')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('Jogador VENCE!'.format(choices[pc]))
    else:
        print('\033[31m', 'Jogada Invalida!', '\033[m')

elif pc == 2:
    if player == 0:
        print('Jogador VENCE!')
    elif player == 1:
        print('Computador VENCE!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('\033[31m', 'Jogada Invalida!', '\033[m')
