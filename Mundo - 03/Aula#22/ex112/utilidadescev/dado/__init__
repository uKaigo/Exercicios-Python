def leiaDinheiro(text):
    tpreco = ""
    while True:
        tpreco = input(text).replace(",", ".")

        if not tpreco.replace(".", "").isnumeric():
            print(f'\033[31m ERRO: "{tpreco}" não é um preço válido.\033[m')
        else:
            break
    return float(tpreco)

        
