sexo = input('Qual seu sexo? (M/F): ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Opção incorreta, tente novamente! (M/F): ').strip().upper()
print('Opção Validada!\nSexo escolhido: "{}"!'.format(sexo))