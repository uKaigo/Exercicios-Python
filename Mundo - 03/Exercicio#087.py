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
print(f'-=' * 30)

s_pares = s3c = m2l = 0
for v, l in enumerate(mat):
    s3c += l[2]
    for c in l:
        if v == 1:
            if c > m2l | c == mat[1][0]:
                m2l = c
        if c % 2 == 0:
            s_pares += c
print(f'A soma dos valores pares é {s_pares}')
print(f'A soma dos valores da terceira coluna é {s3c}')
print(f'O maior valor da segunda linha é {m2l}')
