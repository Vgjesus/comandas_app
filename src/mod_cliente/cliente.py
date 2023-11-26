from flask import Blueprint, render_template, request, redirect, url_for
import requests
from settings import HEADERS_API, ENDPOINT_CLIENTE
from mod_login.login import validaSessao

bp_cliente = Blueprint(
    'cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''


@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    try:
        response = requests.get(ENDPOINT_CLIENTE, headers=HEADERS_API)
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result[0])
        
        return render_template('formListaCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])



@bp_cliente.route('/form-cliente/', methods=['POST','GET'])
@validaSessao
def formCliente():
    return render_template('formCliente.html')

@bp_cliente.route('/edit/<int:id_cliente>', methods=['PUT','GET'])
def formEdit(id_cliente):
    try:
        # Recupera os dados existentes para o cliente específico usando o método GET
        response_get = requests.get(f"{ENDPOINT_CLIENTE}{id_cliente}", headers=HEADERS_API)
        result_get = response_get.json()

        if response_get.status_code != 200:
            raise Exception(result_get[0])

        # Renderiza o formulário de edição com os dados recuperados
        return render_template('formEditCliente.html', cliente=result_get[0][0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_cliente = int(request.form['id'])
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        senha = request.form['senha']

        # monta o JSON para envio a API
        payload = {
            'id_cliente': id_cliente,
            "matricula": "123",
            'nome': nome, 
            'cpf': cpf, 
            'telefone': telefone, 
            'senha': senha,
            "grupo": 4,
        }
        
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_CLIENTE, headers=headers, json=payload)
        result = response.json()
        
        return render_template('formListaCliente.html', msg=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_cliente.route('/update', methods=['POST'])
def update():
    try:
        # dados enviados via FORM
        id_cliente = int(request.form['id'])
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        senha = request.form['senha']

        # monta o JSON para envio a API
        payload = {
            'id_cliente': id_cliente,
            "matricula": "123",
            'nome': nome, 
            'cpf': cpf, 
            'telefone': telefone, 
            'senha': senha,
            "grupo": 4,
        }
        
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # executa o verbo put da API e armazena seu retorno
        url = f"{ENDPOINT_CLIENTE}{id_cliente}"
        response = requests.put(url, headers=headers, json=payload)
        result = response.json()
        
        return render_template('formListaCliente.html', msg=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])


@bp_cliente.route('/cliente/remove/<int:id_cliente>', methods=['GET'])
def remove_cliente(id_cliente):
    try:
        # Envia uma solicitação DELETE para remover o cliente
        response_delete = requests.delete(f"{ENDPOINT_CLIENTE}{id_cliente}", headers=HEADERS_API)
        result_delete = response_delete.json()

        if response_delete.status_code != 200:
            raise Exception(result_delete[0])

        # Redireciona para a lista de clientes após a remoção bem-sucedida
        return redirect(url_for('cliente.formListaCliente'))

    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])