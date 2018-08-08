pes = float(input('Insira seu peso: (KG) '))
alt = float(input('Insira sua altura: (M) '))
est = ''
imc = pes / (alt ** 2)

if imc < 18.5:
    est = 'Abaixo do peso.'
elif 18.5 <= imc < 25:
    est = 'Peso ideal.'
elif 25 <= imc < 30:
    est = 'Sobrepeso.'
elif 30 <= imc < 40:
    est = 'Obesidade.'
elif imc > 40:
    est = 'Obesidade MORBIDA!, cuidado!'

print('O IMC é: {:.1f}\nEstado: {}'.format(imc, est))
