def area(lar, comp):
    m2 = lar * comp
    print(f'A área de um terreno {lar}x{comp} é de {m2}m²')


print('Controle de Terrenos')
print('-' * 20)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)