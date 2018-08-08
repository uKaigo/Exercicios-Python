frase = input('Digite uma frase: ').strip().upper()
palav = frase.split()
junto = ''

for c in range(0, len(palav)):
    junto += palav[c]

inver = junto[::-1]
junto = junto.upper()
inver = inver.upper()
print('{} ao contrário é: {}'.format(junto, inver))
if junto == inver:
    print('E por isso É UM PALÍNDROMO!')
else:
    print('E por isso NÃO É UM PALÍNDROMO')
