n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))

m = (n1 + n2) / 2
print('\nA média entre as notas {:.1f} e {:.1f} do aluno é de {:.1f}'.format(n1, n2, m), end=':\n')
# aprovação ou reprovação
if m >= 6.0:
    print('Aprovado :)')
else:
    print('Reprovado :(')

