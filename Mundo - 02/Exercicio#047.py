print('Todos os números pares de 1 á 50: ')

# cor separador
print('\033[32m', end='')
print('|', end=' ')

for n in range(2, 51, 2):
    print('\033[31m', end='')
    print(n, end=' ')

    # cor separador
    print('\033[32m', end='')
    print('|', end=' ')

print('\033[m\nAcabou')
