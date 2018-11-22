def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = dict()
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['média'] = float(f'{sum(notas)/len(notas):.1f}')
    if sit:
        if dic['média']<5:
            dic['situação'] = 'Ruim'
        elif dic['média']<7:
            dic['situação'] = 'Razoável'
        else:
            dic['situação'] = 'Boa'

    return dic


# Programa Principal
print('-' * 30)
resp = notas(3, 10, 9.1, 4.7, 9, 4.5, 9.4, 8, sit=True)
print(resp)
# help(notas)