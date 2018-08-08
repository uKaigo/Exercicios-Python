# V - !
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
       , 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 á 20: '))
while n not in range(0, 21):
    n = int(input('Tente novamente. Digite um número entre 0 á 20: '))
print(f'Você digitou o número {num[n]}!')
exit()
# V - 2:


num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
       , 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 á 20: '))
    while n not in range(0, 21):
        n = int(input('Tente novamente. Digite um número entre 0 á 20: '))
    print(f'Você digitou o número {num[n]}!')
    start = input('Quer continuar? [S/N] ')
    while start not in 'SsNn':
        start = input('Quer continuar? [S/N] ')
    if start in 'Nn':
        break
print('Programa finalizado.')