import requests

url = 'http://127.0.0.1:8000/clientes/'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

data = {
    "id_cliente": 0,
    "nome": "string",
    "matricula": "string",
    "cpf": "string",
    "telefone": "string",
    "grupo": 0,
    "senha": "string"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
