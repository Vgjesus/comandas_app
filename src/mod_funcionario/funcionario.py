from wsgiref import headers
from flask import Blueprint, render_template, request, redirect, url_for
import requests
from funcoes import Funcoes
import base64
from settings import HEADERS_API, ENDPOINT_FUNCIONARIO
from mod_login.login import validaSessao

bp_funcionario = Blueprint(
    'funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' rotas dos formulários '''


@bp_funcionario.route('/', methods=['GET', 'POST'])
def formListaFuncionario():
    try:
        response = requests.get(ENDPOINT_FUNCIONARIO, headers=HEADERS_API)
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result[0])
        
        return render_template('formListaFuncionario.html', result=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])



@bp_funcionario.route('/form-funcionario/', methods=['POST','GET'])
@validaSessao
def formFuncionario():
    return render_template('formFuncionario.html')


@bp_funcionario.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = request.form['senha']

        # monta o JSON para envio a API
        payload = {
            'id_funcionario': id_funcionario, 
            'nome': nome, 
            'matricula': matricula, 
            'cpf': cpf, 
            'telefone': telefone,
            'grupo': grupo,
            'senha': senha
        }

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_FUNCIONARIO, headers=headers, json=payload)
        result = response.json()

        return render_template('formListaProduto.html', msg=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])


@bp_funcionario.route('/edit/<int:id_funcionario>', methods=['PUT','GET'])
def formEdit(id_funcionario):
    try:
        # Recupera os dados existentes para o funcionário específico usando o método GET
        response_get = requests.get(f"{ENDPOINT_FUNCIONARIO}{id_funcionario}", headers=HEADERS_API)
        result_get = response_get.json()

        if response_get.status_code != 200:
            raise Exception(result_get[0])

        # Renderiza o formulário de edição com os dados recuperados
        return render_template('formEditFuncionario.html', funcionario=result_get[0][0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])

@bp_funcionario.route('/update', methods=['POST'])
def update():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = request.form['senha']

        # monta o JSON para envio a API
        payload = {
            'id_funcionario': id_funcionario, 
            'nome': nome, 
            'matricula': matricula, 
            'cpf': cpf, 
            'telefone': telefone,
            'grupo': grupo,
            'senha': senha
        }

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # executa o verbo put da API e armazena seu retorno
        url = f"{ENDPOINT_FUNCIONARIO}{id_funcionario}"
        response = requests.put(url, headers=headers, json=payload)
        result = response.json()
        
        return render_template('formListaCliente.html', msg=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])

@bp_funcionario.route('/funcionario/remove/<int:id_funcionario>', methods=['GET'])
def remove_funcionario(id_funcionario):
    try:
        # Envia uma solicitação DELETE para remover o cliente
        response_delete = requests.delete(f"{ENDPOINT_FUNCIONARIO}{id_funcionario}", headers=HEADERS_API)
        result_delete = response_delete.json()

        if response_delete.status_code != 200:
            raise Exception(result_delete[0])

        # Redireciona para a lista de funcionarios após a remoção bem-sucedida
        return redirect(url_for('funcionario.formListaFuncionario'))

    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])