from wsgiref import headers
from flask import Blueprint, render_template, request, redirect, url_for
import requests
from funcoes import Funcoes
import base64
from settings import HEADERS_API, ENDPOINT_PRODUTO
from mod_login.login import validaSessao

bp_produto = Blueprint(
    'produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''


@bp_produto.route('/', methods=['GET', 'POST'])
def formListaProduto():
    try:
        response = requests.get(ENDPOINT_PRODUTO, headers=HEADERS_API)
        result = response.json()

        if (response.status_code != 200):
            raise Exception(result[0])
        
        return render_template('formListaProduto.html', result=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])



@bp_produto.route('/form-produto/', methods=['POST','GET'])
@validaSessao
def formProduto():
    return render_template('formProduto.html')


@bp_produto.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_produto = request.form['id_produto']
        nome = request.form['nome']
        descricao = request.form['descricao']

        valor_unitario = request.form['valor_unitario']
                                      
        # monta o JSON para envio a API
        payload = {
            'id_produto': id_produto, 
            'nome': nome, 
            'descricao': descricao, 
            'valor_unitario': valor_unitario,
            "grupo": "4"
        }
        
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_PRODUTO, headers=headers, json=payload)
        result = response.json()

        return render_template('formListaProduto.html', msg=result[0])
    
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])

@bp_produto.route('/edit/<int:id_produto>', methods=['PUT','GET'])
def formEdit(id_produto):
    try:
        # Recupera os dados existentes para o produto específico usando o método GET
        response_get = requests.get(f"{ENDPOINT_PRODUTO}{id_produto}", headers=HEADERS_API)
        result_get = response_get.json()

        if response_get.status_code != 200:
            raise Exception(result_get[0])

        # Renderiza o formulário de edição com os dados recuperados
        return render_template('formEditProduto.html', produto=result_get[0][0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])

@bp_produto.route('/update', methods=['POST'])
def update():
    try:
        # dados enviados via FORM
        id_produto = request.form['id_produto']
        nome = request.form['nome']
        descricao = request.form['descricao']

        valor_unitario = request.form['valor_unitario']
                                      
        # monta o JSON para envio a API
        payload = {
            'id_produto': id_produto, 
            'nome': nome, 
            'descricao': descricao, 
            'valor_unitario': valor_unitario,
            "grupo": "4"
        }
        
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # executa o verbo put da API e armazena seu retorno
        url = f"{ENDPOINT_PRODUTO}{int(id_produto)}"

        response = requests.put(url, headers=headers, json=payload)
        result = response.json()
        
        return render_template('formListaProduto.html', msg=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])

@bp_produto.route('/produto/remove/<int:id_produto>', methods=['GET'])
def remove_produto(id_produto):
    try:
        # Envia uma solicitação DELETE para remover o produto
        response_delete = requests.delete(f"{ENDPOINT_PRODUTO}{id_produto}", headers=HEADERS_API)
        result_delete = response_delete.json()

        if response_delete.status_code != 200:
            raise Exception(result_delete[0])

        # Redireciona para a lista de produtos após a remoção bem-sucedida
        return redirect(url_for('produto.formListaProduto'))

    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])