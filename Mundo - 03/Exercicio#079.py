cont = ''
lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        print('Valor adicionado com sucesso...')
        lista.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = input('Quer continuar? [S/N] ').upper()[0]
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ').upper()[0]
    if cont == 'N':
        break
print('=-' * 30)
print(f'Você digitou os valores {sorted(lista)}')
