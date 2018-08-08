n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tup = (n1, n2, n3, n4)

print(f'Você digitou os valores {tup}')
print(f'O valor 9 apareceu {tup.count(9)} vezes')
if 3 in tup:
    print(f'O valor 3 apareceu na {tup.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for c in tup:
    if c % 2 == 0:
        print(c, end=' ')