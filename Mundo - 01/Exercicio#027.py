name = input('Qual seu nome inteiro? ').title().split()
pname = name[0]
uname = name[len(name) - 1]
print('Primeiro nome: {}\nUltimo nome: {}'.format(pname, uname))
