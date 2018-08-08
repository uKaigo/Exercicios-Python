from emoji import emojize
from time import sleep
print('Contagem regressiva para o estouro dos fogos: ')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize('Estourando :fireworks:'))
print('BUM! BUM! POWW! ')
