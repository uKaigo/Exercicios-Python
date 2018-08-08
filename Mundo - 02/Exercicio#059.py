val1 = int(input('Digite o 1º valor: '))
val2 = int(input('Digite o 2º valor: '))
menu = 1
while menu != 5:
    print('''O que deseja fazer?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    menu = int(input('>> Sua opção: '))
    if menu == 1:
        som = val1 + val2
        print('A soma de {} + {} é: {}'.format(val1, val2, som))
        print('_=_' * 20)

    elif menu == 2:
        mult = val1 * val2
        print('{} multiplicado por {} é: {}'.format(val1, val2, mult))
        print('_=_' * 10)

    elif menu == 3:
        if val1 > val2:
            maior, mname = val1, 'primeiro valor'
        elif val1 < val2:
            maior, mname = val2, 'segundo valor'
        else:
            maior, mname = 'Não existe', 'os dois são iguais'
        print('O maior desses valores é: {} ({})'.format(maior, mname))
        print('_=_' * 10)
    elif menu == 4:
        ant1, ant2 = val1, val2
        val1 = int(input('Digite o novo 1º valor: '))
        val2 = int(input('Digite o novo 2º valor: '))
        print('Valor 1 alterado de {} para {}\nValor 2 alterado de {} para {}'.format(ant1, val1, ant2, val2))
        print('_=_' * 10)
    else:
        print('Opção Inválida!')
        menu = int(input('>> Tente Novamente: '))
print('Saindo do programa!')