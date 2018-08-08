palavras = ('ortopedista', 'casa', 'prato', 'python', 'curso', 'futuro', 'guanabara', 'aprender', 'escola',
            'online', 'youtube', 'papibaquigrafo')

for pal in palavras:
    vogais = ''
    for letra in pal:
        if letra in 'aeiou':
            vogais += f'{letra} '
    print(f'Na palavra {pal.upper()} temos: {vogais}')