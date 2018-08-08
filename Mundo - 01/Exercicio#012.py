v = float(input('Insira o valor do produto: R$'))
d = int(input('Insira o desconto desejado: %'))

vn = v - (v*d/100)

print('\nO valor R${:.2f} com {}% de desconto passa a ser: R${:.2f} reais.'.format(v, d, vn))
