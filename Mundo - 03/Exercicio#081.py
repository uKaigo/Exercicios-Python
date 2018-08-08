nums = list()
while True:
    nums.append(int(input('Digite um número: ')))
    cont = input('Quer continuar? [S/N] ').upper()[0]
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(nums)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(nums, reverse=True)}')
if 5 in nums:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
