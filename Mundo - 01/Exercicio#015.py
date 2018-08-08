day = int(input('Quandos dias de aluguel? '))
km = float(input('Quantos KM rodados? '))
total = (day * 60) + (km * 0.15)

print('O valor a pagar é de R${:.2f}'.format(total))
