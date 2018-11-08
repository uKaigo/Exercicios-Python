from time import sleep


def maior(* nums):
    qnt = len(nums)
    maior = -500 ** 500
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in nums:
        sleep(0.3)
        print(c, end=' ', flush=True)
        if c > maior:
            maior = c
    print(f'Foram informados {qnt} valores ao todo.')
    print(f'O maior valor informado foi {qnt}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()