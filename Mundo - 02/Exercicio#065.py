maior = -1 ** 10
menor = 1 ** 10
number = 1
soma = 0
num = int(input('Digite um número: '))
continuar = 'S'
while continuar not in 'N':
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    number += 1
    continuar = input('Quer continuar? (S/N) ').upper()
    if 'S' == continuar != 'N':
        num = int(input('Digite outro número: '))

media = soma/number
print('Você digitou {} números!\nA média deles foi {:.2f}\nO maior foi {}\nO menor foi {}'.format(soma, media, maior, menor))