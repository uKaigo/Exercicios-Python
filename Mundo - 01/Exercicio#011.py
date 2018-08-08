larg = float(input('Insira em metros a largura: '))
alt = float(input('Insira em metros a altura: '))

area = larg*alt
lt = area / 2

print('\nUma parede de {} x {} com a área de {}m²\nPrecisaria de {} litros de tinta para se pintar.\n1 litro = 2m²'.format(larg, alt, area, lt))
3