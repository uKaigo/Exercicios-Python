km = int(input('Insira a distância da viagem: '))
if km <= 200.0:
    pay = km * 0.50
else:
    pay = km * 0.45
print('Uma viagem de {}KM custará: R${:.2f} reais!'.format(km, pay))