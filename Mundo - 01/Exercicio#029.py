vel = float(input('Insira sua velocidade: KM'))
if vel > 80.0:
    pag = (vel-80.0)*7
    print('Velocidade de 80 KM/h Excedida!! Valor a pagar: R${:.2f}'.format(pag))
else:
    print('Velocidade permitida! Continue andando nos {:.1f} KM/h'.format(vel))