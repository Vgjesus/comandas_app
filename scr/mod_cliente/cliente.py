from flask import Blueprint, render_template

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''

@bp_cliente.route('/')
def formListaCliente():
    return render_template('formListaCliente.html'), 200

@bp_cliente.route('/form-cliente/', methods=['GET'])
def formCliente():
    return render_template('formListaCliente.html')


'''
Rota antiga de app...
@app.route('/cliente/')
def formListaCliente():
# return "<h1>Rota da página de Clientes da nossa WEB APP</h1>", 200
return render_template('formListaClientes.html'), 200
'''