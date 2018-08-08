"""
 meus miolos foram pro saco kkkk, eu nem sabia como calculava, só vi o padrão:
 0 - 1 - 1 - 2 - 3 - 5 - 8
 ai só vi que o número é a soma do anterior com o posterior, por exemplo, o segundo número 1, é 0 + 1
"""

print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
n = int(input('Quantos termos quer mostrar: '))
a = 1  # é o número anterior, por onde vai começar, se quiser troque
po = 0  # é o número posterior
p = 0  # é o número atual

vez = 0
while vez < n:
    vez += 1
    print(p, end='')
    print(' ➜ ' if vez < n else '', end='')
    po = a  # define o posterior como o anterior
    a = p  # define o anterior como atual
    p = a + po  # define o atual como a soma do po com o a
