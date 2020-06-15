from ex115 import utils, pessoas
import os
 
if not os.path.exists("ex115/pessoas.json"):
    with open("ex115/pessoas.json", "w") as ps: 
        ps.write("[\n\n]")

try: 
    while True: 
        op = utils.printMenu()
        if op == 1:
            utils.printHeader("Pessoas Cadastradas")
            if not pessoas.get():
                print('Nenhuma pessoa cadastrada.')
            else:
                for p in pessoas.get():
                    print(f'{p["nome"]:<30} {p["idade"]:>3} anos')
        elif op == 2:
            utils.printHeader("Novo Cadastro")
            name = utils.leiaNome('Nome: ')
            if name == -1:
                continue
            yo = utils.leiaIdade('Idade: ')
            if yo == -1:
                continue
            pessoa = pessoas.cadastrar(name, yo)
            print(f'Novo registro de {pessoa["nome"]} adicionado.')
        elif op == 3:
            utils.printHeader("Saindo do sistema... Até logo!")
            break
except Exception as e:
    print(f'Algum erro ocorreu [{type(e).__name__}]: {e}')
    utils.printHeader("Saindo do sistema... Até logo!") 
 
