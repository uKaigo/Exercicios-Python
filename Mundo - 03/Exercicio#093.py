jogador = {}

nome = input('Nome do jogador: ')
parts = int(input(f'Quantas partidas {nome} jogou? '))
gols = []
for c in range(parts):
    g = int(input(f'Quantos gols na partida {c}? '))
    gols.append(g)
jogador["nome"] = nome
jogador["gols"] = gols
jogador["total"] = sum(gols)
print('-=' * 30)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}.')
print(f'-=' * 30)
print(f'O jogador {nome} jogou {parts} partidas.')
for c in range(parts):
    print(f'    => Na partida {c}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')