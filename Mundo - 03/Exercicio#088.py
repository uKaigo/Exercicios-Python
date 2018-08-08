from random import sample
from time import sleep
jo = []
print('-' * 30)
print('{:^30}'.format('JOGO NA MEGA SENA'))
print('-' * 30)
games = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {games} JOGOS  -=-=-=')
for c in range(games):
    jo.append(sample(range(1, 60), 6))
for v, c in enumerate(jo):
    print(f'Jogo {v+1}: {sorted(c)}')
    if v != len(jo)-1:
        sleep(1)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')