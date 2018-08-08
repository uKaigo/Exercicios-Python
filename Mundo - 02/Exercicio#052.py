num = int(input('Digite um número inteiro: '))
div = 0

for c in range(1, num+1):
    if num % c == 0:
        div += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print('\033[m')
print('O número {} foi dividido {} vezes!'.format(num, div))

if div == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
