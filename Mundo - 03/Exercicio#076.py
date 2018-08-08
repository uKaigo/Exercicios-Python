lista = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for prod in range(0, len(lista) - 1, 2):
    price = prod + 1  # preço
    print(f'{lista[prod]:.<30}.R${lista[price]:>7.2f}')
print('-' * 40)
