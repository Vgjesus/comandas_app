from wsgiref import headers
from flask import Blueprint, render_template, request
import requests
from funcoes import Funcoes
import base64
from settings import HEADERS_API, ENDPOINT_CLIENTE

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
def formCliente():
    return render_template('formCliente.html')


@bp_cliente.route('/insert', methods=['POST'])
def insert():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id']
        nome = request.form['nome']
        grupo = request.form['grupo']
        senha = request.form['senha']

        #foto = request.form['foto']
        valor_unitario = request.form['valor_unitario']

        # converte a foto em base64
        foto = "data:" + request.files['foto'].content_type + ";base64," + str(base64.b64encode(request.files['foto'].read()), "utf-8")

        # monta o JSON para envio a API
        payload = {'id_cliente': id_cliente, 'nome': nome, 'foto': foto}
        
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(ENDPOINT_CLIENTE, headers=headers, json=payload)
        result = response.json()
        
        return render_template('formListaProduto.html', msg=result[0])
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e.args[0])