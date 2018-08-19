from random import randint
from time import sleep

game = {}

print('Valores sorteados: ')
for c in range(1, 5):
    n = randint(1, 6)
    game[f'jogador{c}'] = n
    print(f'    O jogador{c} tirou {n}')
    sleep(1)

rank = []
for c in game.items():
    rank.append(c)

rank.sort(key=lambda player: player[1], reverse=True)
print('Ranking dos jogadores:')
for c in range(1, 5):
    pl = rank[c-1][0]
    po = rank[c-1][1]
    print(f'    {c}º lugar: {pl} com {po}')
    sleep(1)
