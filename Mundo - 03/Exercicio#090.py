aluno = {}
nome = input('Nome: ')
med = float(input(f'Média de {nome}: '))
if med >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'

aluno["Nome"] = nome
aluno["Média"] = med
aluno["Situação"] = sit

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

