s = float(input('Insira o salário do funcionario: R$'))
a = int(input('Insira o aumento desejado: %'))

sn = s + (s*a/100)
print('\nO funcionário que ganhava R${:.2f} reais, com {}% de aumento passa a ganhar: R${:.2f} reais'.format(s, a, sn))