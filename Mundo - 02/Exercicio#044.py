print(f'{" LOJAS KAIGO ":=^40}')
price = float(input('Insira o valor das compras: R$'))
print('''Formas de pagamento: 
[ 1 ] Á vista dinheiro/cheque.
[ 2 ] Á vista no cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')
op = int(input('Qual é a opção? '))

if op == 1:
    nprice = price - (price*10/100)

elif op == 2:
    nprice = price - (price*5/100)

elif op == 3:
    p = price / 2
    nprice = price
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(p))

elif op == 4:
    nprice = price + (price*20/100)
    p = int(input('Deseja parcelar em quantas vezes? '))
    pricep = nprice / p
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(p, pricep))

else:
    print('\033[31mOpcão Invalida de pagamento!!! \033[4;33mContinuando\033[31m!\033[m')
    nprice = price

print('\nSua compra de R${:.2f} vai custar R${:.2f} reais!'.format(price, nprice))
