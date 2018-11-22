from datetime import date
ano = date.today().year


def voto(idade):
    if 18 <= idade <= 70:
        voto = 'VOTO OBRIGATÓRIO'
    elif 16 <= idade >= 70:
        voto = 'VOTO OPCIONAL'
    else:
        voto = 'NÃO VOTA'
    return voto


# PROGRAMA PRINCIPAL
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc

print(f'Com {idade} anos: {voto(idade)}.')
