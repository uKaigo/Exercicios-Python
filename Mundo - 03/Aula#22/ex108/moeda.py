def metade(coin):
    return coin/2

def dobro(coin):
    return coin*2

def aumentar(coin, pcent):
    return coin + (coin*pcent/100)

def diminuir(coin, pcent):
    return coin - (coin*pcent/100)

def moeda(money):
    return f"R${money:.2f}".replace(".", ",")
