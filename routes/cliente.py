from flask import Blueprint, render_template

"""
Rota de clientes

- /clientes/ (GET) - Listar os clientes
- /clientes/ (POST) - inserir clients no servidor
- /clientes/new (GET) - renderizar formulario para criar um cliente
- /clientes/<id> (GET) - obter os dados de um clientes
- /clientes/<id>/edit (GET) - renderizar um formalulario para editar um cliente
- /clientes/<id>/update (PUT) - atualizar os dados do cliente
- /clientes/<id>/delete (DELETE) - delata o registro do usuario

"""

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route("/")
def lista_clientes():
    # Listar os clientes
    return {'pagina': 'lista_clientes'}

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # inserir clientes no servidor
    pass

@cliente_route.route('/new')
def form_cliente():
 # renderizar formulario para criar um cliente
   return {'pagina': "formulario cliente"}

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    # exibir detalhes do cliente 
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # formulario para editar um cliente
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    # atualizar os dados cliente
    pass

@cliente_route.route('/<int:clinte_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    # deletar um cliente
    pass