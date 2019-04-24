def metade(coin, frmt):
    if format:
        return moeda(coin/2)
    return coin/2

def dobro(coin, frmt):
    if frmt:
        return moeda(coin*2)
    return coin*2

def aumentar(coin, pcent, frmt):
    if frmt:
        return moeda(coin + (coin*pcent/100))
    return coin + (coin*pcent/100)

def diminuir(coin, pcent, frmt):
    if frmt:
        return moeda(coin - (coin*pcent/100))
    return coin - (coin*pcent/100)

def moeda(coin):
    return f"R${coin:.2f}".replace(".", ",")

def resumo(coin, add, sub):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<15}', end='')
    print(f'{moeda(coin):>15}')
    print(f'{"Dobro do preço:":<15}', end='')
    print(f'{dobro(coin, True):>15}')
    print(f'{"Metade do preço:":<15}', end='')
    print(f'{metade(coin, True):>15}')
    almnt = f'{add}% de aumento:'
    print(f'{almnt:<15}', end='')
    print(f'{aumentar(coin, add, True):>15}')
    rdco = f'{sub}% de redução:'
    print(f'{rdco:<15}', end='')
    print(f'{diminuir(coin, sub, True):>15}')
    print('-'*30)
