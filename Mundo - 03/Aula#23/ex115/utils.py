from os import system
def leiaIdade(prompt='Digite um número inteiro: '): # Leia Int
    num = -1
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                raise ValueError
        except (ValueError, NameError): #NameError pq quando digitava letra dava isso
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu cancelar.\033[m')
            break
        else:
            break
    return num

def leiaNome(prompt='Digite um texto: '):
    nome = -1
    while True:
        try:
            nome = input(prompt)
            if not len(nome) > 1:
                raise NameError
        except NameError:
            print('\n\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu cancelar.\033[m')
            break
        else:
            break
    return nome

def printHeader(text="MENU"):
    print('-'*42)
    print(f'{text.upper():^42}')
    print('-'*42)

def printMenu():
    while True:
        printHeader("Menu Principal")
        print('\033[33m1 \033[m- \033[34mVer pessoas cadastradas')
        print('\033[33m2 \033[m- \033[34mCadastrar nova Pessoa')
        print('\033[33m3 \033[m- \033[34mSair do Sistema\033[m')
        print('-'*42)
        try:
            op = int(input("\033[32mSua Opção: \033[m"))
            if op not in range(1, 4):
                raise ValueError
        except (ValueError, NameError):
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        except KeyboardInterrupt:
            print('')
            return 3
        else:
            return op
