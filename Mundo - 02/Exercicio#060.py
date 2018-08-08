# _-_= WHILE =_-_ #
num = int(input('Digite um para ver o fatorial: '))
print('Calculando \033[36m{}! \033[m= '.format(num), end='')
c = num
r = 1
while c > 0:
    print(c, end=' x ' if c > 1 else ' =')
    r *= c
    c -= 1
print('\033[36m', r)

# _-_= FOR =_-_ #
num = int(input('Digite um para ver o fatorial: '))
print('Calculando \033[36m{}! \033[m= '.format(num), end='')
c = num
r = 1
for co in range(num, 0, -1):
    print(c, end=' x ' if c > 1 else ' =')
    r *= c
    c -= 1
print('\033[36m', r)
