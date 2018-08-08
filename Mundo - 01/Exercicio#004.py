var = input('Digite algo: ')

print('\nInformações da variavel "{}"\n'.format(var))
print('Tipo:', type(var))
print('Tem apenas espaços?', var.isspace())
print('É alfabetico?', var.isalpha())
print('É numerico?', var.isnumeric())
print('É alfanumerico?', var.isalnum())
print('Está em maiusculo?', var.isupper())
print('Está em minusculo?', var.islower())
print('Está Capitalizado?', var.istitle())

