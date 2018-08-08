mat = []
li = []
for l in range(3):
    for c in range(3):
        li.append(int(input(f'Digite um número para [{l}, {c}]: ')))
    mat.append(li)
    li = []
print('-=' * 30)
for l in mat:
    for c in l:
        print(f'[ {c} ]', end='')
    print('')
