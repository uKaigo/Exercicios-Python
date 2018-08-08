phrase = input('Digite uma frase: ').upper().strip()
a = phrase.count('A')
pa = phrase.find('A') + 1
ua = phrase.rfind('A') + 1
print('"A" aparece {} vezes\nO primeiro aparece na posição: {}A\nE o ultimo na posição: {}'.format(a, pa, ua))