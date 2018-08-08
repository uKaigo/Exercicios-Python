print('Soma números impares multiplos de 3 entre 1 e 500')
num = 0
val = 0
for n in range(3, 501, 3):
    if n % 2 != 0:
        num += n
        val += 1
print('A soma entre {} números foi: {}'.format(val, num))
