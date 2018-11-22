def leiaInt(prompt=None):
    if prompt is None:
        prompt = 'Digite um número: '
    inpt = input(prompt)
    while not inpt.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        inpt = input(prompt)
    return int(inpt)


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
