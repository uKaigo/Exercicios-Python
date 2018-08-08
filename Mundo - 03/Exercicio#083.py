exp = input('Digite uma expressão: ')
parent = []
pa = 0
for p in exp:
    if p in '()':
        parent.append(p)
for p in parent:
    if p == ')' and pa == 0:
        pa -= 1
        break
    if p == '(':
        pa += 1
    else:
        pa -= 1
if pa != 0:
    print(f'Sua expressão está inválida!')
else:
    print(f'Sua expressão está válida!')