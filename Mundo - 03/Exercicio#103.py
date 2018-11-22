def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome.strip()} fez {gols} gol(s) no campeonato.')


# Programa Principal

print('-' * 30)
name = input('Nome do Jogador: ')
goals = input('Número de Gols: ')

ficha(name, goals)