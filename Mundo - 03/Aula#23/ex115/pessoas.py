import json
import os
def cadastrar(name, yearso: int):
    if not os.path.exists("ex115/pessoas.json"):
        with open("ex115/pessoas.json", "w") as ps:
            ps.write("[\n\n]")
    with open("ex115/pessoas.json") as ps:
        pessoas = json.loads(ps.read())
    with open("ex115/pessoas.json", "w") as ps:
        pessoas.append({"nome": name.title(), "idade": yearso})
        ps.write(json.dumps(pessoas, indent=4, sort_keys=False))
    with open("ex115/pessoas.json") as ps:
        pessoas = json.loads(ps.read())
    return pessoas[-1]

def get():
    if not os.path.exists("ex115/pessoas.json"):
        with open("ex115/pessoas.json", "w") as ps:
            ps.write("[\n\n]")
    with open("ex115/pessoas.json") as ps:
        return json.loads(ps.read())
