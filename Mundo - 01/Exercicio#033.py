n1 = int(input('Insira o primeiro número: '))
n2 = int(input('O segundo: '))
n3 = int(input('Terceiro: '))
print('')

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if (maior+menor) > n3:
    maior = maior
    menor = n3
else:
    maior = n3
    menor = menor

print('O maior é: {}\nO menor é: {}'.format(maior, menor))