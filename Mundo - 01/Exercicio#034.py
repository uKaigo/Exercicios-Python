sal = float(input('Insira o salário do funcionario: R$'))

if sal > 1250.00:
    au = 10
    nv = sal + (sal * au / 100)
else:
    au = 15
    nv = sal + (sal * au / 100)
print('O salário de R${:.2f} com {}% de aumento é:\nR${:.2f}'.format(sal, au, nv))
