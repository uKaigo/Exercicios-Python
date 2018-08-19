from datetime import datetime
anoa = datetime.today().year
pessoa = {}

nome = input('Nome: ')
anon = int(input('Ano de nascimento: '))
idade = anoa - anon
ctps = int(input('Carteira de Trabalho (0 não tem): '))

pessoa['nome'] = nome
pessoa['idade'] = idade
pessoa['ctps'] = ctps

if ctps != 0:
    anoc = int(input('Ano de contratação: '))
    sal = float(input('Salário: R$ '))
    pessoa['contratação'] = anoc
    pessoa['salário'] = sal

    aposent = anoc + 35
    aposent -= anon
    pessoa['aposentadoria'] = aposent

print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')