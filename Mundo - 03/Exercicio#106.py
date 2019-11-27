from time import sleep
  
def escreva(cor, texto): 
    tam = len(texto)+4
    print(f'\033[{cor+10}m', end='')
    print('~'*tam)
    print(f'  {texto}')
    print('~'*tam, end='\n\033[m')


# Programa Principal
while True: 
    escreva(32, 'SISTEMA DE AJUDA PyHELP')
    sleep(1)
    func = input('Função ou Biblioteca > ')
    if func.upper() == 'FIM':
        escreva(35, "ATÉ LOGO!")
        break
    sleep(1)
    escreva(34, f"Acessando o manual do comando '{func}'")
    sleep(0.5)
    print('\033[41m', end='')
    help(func)
    sleep(1)
