l1 = []
l2 = []
l3 = []
while True:
    n = int(input('Digite um número: '))
    l1.append(n)
    cont = input('Quer continuar? [S/N] ').upper()[0]
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
for v in l1:
    if v % 2 == 0:
        l2.append(v)
    else:
        l3.append(v)
print('-=' * 30)
print(f'A lista completa é {l1}')
print(f'A lista de pares é {l2}')
print(f'A lista de ímpares é {l3}')
