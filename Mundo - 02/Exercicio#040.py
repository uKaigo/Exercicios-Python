n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))

nota = (n1+n2) / 2
est = ''
if nota < 5.0:
    est = 'REPROVADO'
elif 5.0 <= nota <= 6.9:
    est = 'RECUPERAÇÃO'
elif nota >= 7.0:
    est = 'APROVADO!'

print('Este aluno teve a média de {:.1f} e o estado dele é: {}!'.format(nota, est))
