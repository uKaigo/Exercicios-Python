def leiaInt(prompt='Digite um número inteiro: '):
    num = 0
    while True:
        try:
            num = int(input(prompt))
        except (ValueError, NameError): #NameError pq quando digitava letra dava isso
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            break
        else:
            break
    return num
def leiaFloat(prompt='Digite um número real: '):
    num = 0
    while True:
        try:
            num = float(input(prompt))
        except (ValueError, TypeError, NameError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
            break
        else:
            break
    return num
inte = leiaInt("Digite um Inteiro: ")
real = leiaFloat("Digite um Real: ")
print(f"O valor inteiro digitado foi {inte} e o real foi {real}")