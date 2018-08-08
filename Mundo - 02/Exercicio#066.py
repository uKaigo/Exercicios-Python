val = soma = 0
while True:
    n = int(input('Digite um valor (999 PARA): '))
    if n == 999:
        break
    val += 1
    soma += n
print(f'A soma dos {val} valores foi {soma}!')
