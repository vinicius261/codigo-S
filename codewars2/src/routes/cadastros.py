


from flask import Blueprint, jsonify, request

from src.cadastro import CadastroFuncionarios

cadastros = Blueprint('cadastro', __name__)


cadastro = CadastroFuncionarios()


@cadastros.route("/cadastro", methods=['POST'])
def cadastrar_funcionario():

    dados = request.json

    cadastro.cadastrar(dados['nome'], dados['cpf'], dados['data_admissao'], dados['cargo'],)

    return "ok", 201


@cadastros.route("/cadastro/<matricula>")
def consultar_funcionario(matricula):
    
    funcionario = cadastro.consultar(matricula)

    resposta = {
        'matricula': funcionario.matricula,
        'nome': funcionario.nome,
        'cpf': funcionario.cpf,
        'data_admissao': funcionario.data_admissao,
        'cargo': cadastro.convert_json_saida(funcionario.cargo),
    }

    return jsonify(resposta)


@cadastros.route("/cadastro/<matricula>", methods=['DELETE'])
def excluir_funcionario(matricula):
    
    cadastro.excluir(matricula)

    return ' ', 204


@cadastros.route("/cadastro/<matricula>", methods=['PATCH'])
def alterar_funcionario(matricula):

    dados_escolhidos = request.json

    cadastro.alterar(matricula, dados_escolhidos)

    return "ok", 201


@cadastros.route("/cadastro")
def listar_todos():

    funcionarios = cadastro.listar_todos()

    resposta = list(map(lambda x: {
        "matricula": x.matricula,
        "nome": x.nome,
        "cpf": x.cpf,
        "data_admissao": x.data_admissao,
        "cargo": cadastro.convert_json_saida(x.cargo)},
        funcionarios))

    return jsonify(resposta)

