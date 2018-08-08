vals = [[], []]
#       P   I
for c in range(7):
    v = int(input(f'Digite o {c+1}o. valor: '))
    if v % 2 == 0:
        vals[0].append(v)
    else:
        vals[1].append(v)
print('-=' * 30)
print(f'Os valores pares digitados foram: {vals[0]}')
print(f'Os valores ímpares digitados foram: {vals[1]}')
