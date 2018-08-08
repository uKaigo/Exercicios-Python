num = int(input('Digite um número inteiro: '))
print('''Deseja converter o número {} para o que?
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal
'''.format(num))
op = int(input('Sua opção: '))

if op == 1:
    print('O número {} convertido para Binário é: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para Octal é: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para Hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!!!')
