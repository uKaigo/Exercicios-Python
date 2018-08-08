cval = float(input('Insira o valor da casa: R$'))
cosal = float(input('Insira o salario do comprador: R$'))
anos = int(input('Em quantos anos ele vai pagar? '))

total = cval / (anos * 12)
min = cosal * 30 / 100

print('\nPara pagar uma casa de R${:.2f} em {} anos.'.format(cval, anos), end=' ')
print('Tera que pagar: R${:.2f} de prestação.'.format(total))
if total <= min:
    print('Emprestimo ACEITO!\nO mínimo era: R${:.2f}.'.format(min))
else:
    print('Emprestimo NEGADO!\nO mínimo é: R${:.2f}.'.format(min))
