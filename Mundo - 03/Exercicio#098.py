from time import sleep


def contador(inicio, fim, passo):
    passo *= -1 if passo < 0 else 1
    passo = 1 if passo == 0 else passo
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            sleep(0.5)
            print(c, end=' ', flush=True)
        print('FIM!')
    else:
        passo = passo * -1
        for c in range(inicio, fim-1, passo):
            sleep(0.5)
            print(c, end=' ', flush=True)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
strt = int(input('Inicio: '))
end = int(input('Fim: '))
stp = int(input('Passo: '))

contador(strt, end, stp)