s1 = float(input('Insira o primeiro segmento: '))
s2 = float(input('Insira o segundo segmento: '))
s3 = float(input('Insira o terceiro segmento: '))
tri = ''
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        tri = 'EQUILATERO'
    elif s1 == s2 or s2 == s3 or s3 == s1:
        tri = 'ISOSCELES'
    elif s1 != s2 != s3:
        tri = 'ESCALENO'

    print('Os segmentos podem formar um triângulo: {}'.format(tri))
else:
    print('Os segmentos não podem formar um triângulo!')
