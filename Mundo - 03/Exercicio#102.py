def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor Fatorial de um número n.
    """

    txt = ''
    res = 1
    for c in range(n, 0, -1):
        res *= c
        if show:
            txt += f'{c} x ' if c > 1 else f'{c} = {res}'
        else:
            txt = res
    return txt


# Programa Principal

print(fatorial(5, True))
# help(fatorial)
