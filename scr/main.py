from flask import Flask
from settings import HOST, PORT, DEBUG
from flask import Flask, render_template

# import blueprint criado
from mod_cliente.cliente import bp_cliente

# import blueprint criado
from mod_funcionario.funcionario import bp_funcionario

# import blueprint criado
from mod_index.index import bp_index

# import blueprint criado
from mod_produto.produto import bp_produto

app = Flask(__name__)

# registro das rotas do blueprint
app.register_blueprint(bp_cliente)

# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)

# registro das rotas do blueprint
app.register_blueprint(bp_index)

# registro das rotas do blueprint
app.register_blueprint(bp_produto)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host=HOST, port=PORT, debug=DEBUG)