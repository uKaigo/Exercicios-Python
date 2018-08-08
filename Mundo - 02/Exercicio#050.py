cont = 0
som = 0
for n in range(1, 7):
    nu = int(input('Digite outro número inteiro: '))
    if nu % 2 == 0:
        som += nu
        cont += 1
print('Você informou {} números pares e a soma deles é: {}'.format(cont, som))