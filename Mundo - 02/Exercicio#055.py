pesos = [float(input('Peso da {}ª pessoa: '.format(p))) for p in range(1, 6)]
print('\nMaior peso lido: {:.1f}Kg\nMenor peso lido: {:.1f}Kg'.format(max(pesos), min(pesos)))
