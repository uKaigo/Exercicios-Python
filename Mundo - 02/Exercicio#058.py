from random import randint
# pensa em um número
pc = randint(0, 10)
# pergunta o número ao jogador
user = int(input('Pensei em um número de 0 - 10! Qual você pensa que é? '))
tent = 1
# seta o plural
plural = ''
# enquanto o jogador não acertar
while user != pc:
    # seta o plural
    plural = 's'
    if user > pc:
        m_o_m = 'menor'
    else:
        m_o_m = 'maior'
    tent += 1
    user = int(input('Errou! Chute em um número {}: '.format(m_o_m)))
print('Acertou! Você chegou a esta resposta com {} tentativa{}!'.format(tent, plural))
