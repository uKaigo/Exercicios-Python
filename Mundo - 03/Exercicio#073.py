sep = f'{"-=" * 15}'
times = ('Flamengo', 'São Paulo', 'Corinthians', 'Fluminense', 'Internacional', 'Sport Recife', 'Cruzeiro', 'Atlético',
         'Grêmio', 'Palmeiras', 'Vasco da Gama', 'América-MG', 'Atlético-PR', 'Botafogo', 'Chapecoense', 'EC Vitória',
         'Bahia', 'Santos', 'Ceará SC', 'Paraná')

print(sep)
print('Lista de times do Brasileirão:', times)
print(sep)
print(f'Os 5 primeiros são {times[:5]}')
print(sep)
print(f'Os 4 últimos são {times[-4:]}')
print(sep)
print(f'Times em ordem alfabética: {sorted(times)}')
print(sep)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}º posição.')
