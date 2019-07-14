import requests
try:
    requests.get("http://www.pudim.com.br")
except:
    print("\033[31mO site Pudim não está acessível no momento.")
else:
    print("\033[32mConsegui acessar o site Pudim com sucesso!") 
