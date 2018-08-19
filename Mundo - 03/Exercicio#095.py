jogadores = []
while True:
    jogador = {}
    print('-' * 30)
    nome = input('Nome do jogador: ')
    parts = int(input(f'Quantas partidas {nome} jogou? '))
    gols = []
    for c in range(parts):
        g = int(input(f'Quantos gols na partida {c}? '))
        gols.append(g)
    jogador["nome"] = nome
    jogador["gols"] = gols
    jogador["total"] = sum(gols)
    jogadores.append(jogador)
    cont = input('Quer continuar? [S/N] ')[0]
    if cont in 'Nn':
        break
print('-=' * 41)
print('cod nome            gols           total')
print('-' * 41)
for c in range(len(jogadores)):
    jogador = jogadores[c]
    print(f'{c:>3} {jogador["nome"]:<15} {str(jogador["gols"]):<14} {jogador["total"]}')
while True:
    print('-' * 41)
    jo = int(input('Mostrar dados de qual jogador? '))
    if jo == 999:
        break
    if jo >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {jo}! Tente novamente')
    else:
        jogador = jogadores[jo]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["nome"]}')
        for c in range(len(jogador["gols"])):
            print(f'    No jogo {c} fez {jogador["gols"][c]} gols.')
print('<<< Volte sempre >>>')