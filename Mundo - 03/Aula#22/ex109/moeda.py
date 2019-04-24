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
