som = dig = 0
num = int(input('Digite um número (999 para): '))
while num != 999:
    som += num
    dig += 1
    num = int(input('Digite outro número (999 para): '))
print('Você digitou {} número(s), e a soma deles foi: {}'.format(dig, som))