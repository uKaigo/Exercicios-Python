lista = []
for c in range(5):
    n = int(input('Número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O número foi adicionado no final da lista...')
    else:
        for i in range(len(lista)):
            if n <= lista[i]:
                lista.insert(i, n)
                print(f'O número foi adicionado na posição {i} da lista...')
                break
print(f'Os valores digitados em ordem foram: {lista}')
