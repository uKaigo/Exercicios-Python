alunos = []
while True:
    aluno = []
    nts = []
    n = input('Nome: ')
    nts.append(float(input('Nota 1: ')))
    nts.append(float(input('Nota 2: ')))
    aluno.append(n)
    aluno.append(nts)
    aluno.append(sum(nts)/2)  # achei depois esse comando (soma a lista)
    alunos.append(aluno)

    cont = input('Quer continuar? [S/N] ')[0]
    if cont in 'Nn':
        break
print('-=' * 30)
print('No. NOME        MÉDIA')
print('-' * 25)
for n, a in enumerate(alunos):
    print(f'{n:<2}  {a[0]:<12} {a[2]:.1f}')
print('-' * 35)
while True:
    i = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    while i >= len(alunos) and i != 999:
        i = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if i == 999:
        print('FINALIZANDO...')
        break
    aluno = alunos[i]
    print(f'Notas de {aluno[0]} são {aluno[1]}')
    print('-' * 35)
print('<<< VOLTE SEMPRE >>>')