total = m1000 = 0
mbarato = 1500 ** 1500
mbarato_n = ''
print('-' * 45)
print(f'{"LOJA SUPER BARATÃO":^45}')
print('-' * 45)
while True:
    prod_name = str(input('Nome do produto: ')).strip()
    prod_price = float(input('Preço do produto: R$'))
    total += prod_price
    if prod_price > 1000.00:
        m1000 += 1
    if prod_price < mbarato:
        mbarato_n = prod_name
        mbarato = prod_price
    continue_ = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continue_ not in 'SN':
        continue_ = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continue_ == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^45}')
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {m1000} produtos custando mais de R$1000.00 reais.')
print(f'O produto mais barato foi o(a) {mbarato_n} que custa R${mbarato:.2f}')