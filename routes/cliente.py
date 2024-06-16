from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

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
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # inserir clientes no servidor
    
    data = request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }

    CLIENTES.append(novo_usuario)


    return render_template('item_cliente.html', clientes=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
 # renderizar formulario para criar um cliente
   return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    # exibir detalhes do cliente 
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # formulario para editar um cliente
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    # atualizar os dados cliente
    pass

@cliente_route.route('/<int:clinte_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    # deletar um cliente
    pass