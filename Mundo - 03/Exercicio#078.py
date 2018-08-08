lis = list()
for c in range(0, 5):
    n = int(input(f'Digite um valor para a posição {c}º: '))
    lis.append(n)
ma = max(lis)
me = min(lis)
print('=-' * 30)
print(f'Você digitou os valores {lis}')
print(f'O maior valor digitado foi {ma} nas posições ', end='')
for p, n in enumerate(lis):
    if n == ma:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {me} nas posições ', end='')
for p, n in enumerate(lis):
    if n == me:
        print(f'{p}... ', end='')
