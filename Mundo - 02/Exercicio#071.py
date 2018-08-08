valor = int(input('Valor para sacar: '))
c50 = c20 = c10 = c1 = 0

while valor >= 50:
    valor -= 50
    c50 += 1
while valor >= 20:
    valor -= 20
    c20 += 1
while valor >= 10:
    valor -= 10
    c10 += 1
while valor >= 1:
    valor -= 1
    c1 += 1
if c50 != 0:
    print(f'Cedulas de R$50: {c50}')
if c20 != 0:
    print(f'Cedulas de R$20: {c20}')
if c10 != 0:
    print(f'Cedulas de R$10: {c10}')
if c1 != 0:
    print(f'Cedulas de R$1: {c1}')