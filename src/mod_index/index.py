from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, url_prefix="/home", template_folder='templates')

''' rotas dos formulários '''

@bp_index.route('/', methods=['GET', 'POST'])
def formListaIndex():
    return render_template('formIndex.html'), 200

# @bp_index.route('/', methods=['GET'])
@bp_index.route('/')
def formIndex():
    # return render_template('formListaIndex.html')
    return render_template('formIndex.html'), 200



'''
Rota antiga de app...
@app.route('/index/')
def formListaIndex():
# return "<h1>Rota da página de Index da nossa WEB APP</h1>", 200
return render_template('formListaIndex.html'), 200
'''