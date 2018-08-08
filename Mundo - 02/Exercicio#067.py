while True:
    n = int(input('Digite um número para ver sua tabuada (negativo para): '))
    if n < 0:
        break
    print('-' * 25)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 25)
print('Programa tabuada encerrado! Volte sempre!')
