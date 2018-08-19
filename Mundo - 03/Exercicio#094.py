pessoas = []
ids = 0
while True:
    pessoa = {}
    no = input('Nome: ')
    sex = input('Sexo: [M/F] ')[0]
    idad = int(input('Idade: '))
    ids += idad
    pessoa["nome"] = no
    pessoa["sexo"] = sex
    pessoa["idade"] = idad
    pessoas.append(pessoa)
    cont = input('Quer continuar? [S/N] ')[0]
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
med = ids/len(pessoas)
print(f'- A média de idade é de {med} anos.')
print(f'- As mulheres cadastradas foram: | ', end='')
for p in pessoas:
    if p["sexo"] in 'Ff':
        print(p["nome"], end=' | ')
print()
print(f'- Lista das pessoas que estão acima da média:\n ')

for p in pessoas:
    if p["idade"] > med:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('\n ')

print('<< ENCERRADO >>')
