


from flask import Blueprint, jsonify, request
from src.cadastro import CadastroFuncionarios
from src.funcionarios import Funcionario

from src.holerites import Holerite

holerite = Blueprint('holerite', __name__)

cadastro = CadastroFuncionarios()

@holerite.route("/holerite/<matricula>/<mes>/<faltas>")
def novo_holerite(matricula, mes, faltas):

    funcionario = cadastro.consultar(matricula)

    holerite_inst = Holerite(funcionario)
    
    conteudo_holerite = holerite_inst.gerar_holerite(mes, faltas)

    resposta = {
                'Funcionário': funcionario.nome,
                'Matricula' : funcionario.matricula,
                'Data da Admissão': funcionario.data_admissao,
                'Cargo': funcionario.cargo.descricao,
                'ano': conteudo_holerite.ano,
                'mes': conteudo_holerite.mes,
                'faltas': conteudo_holerite.faltas,
                'desconto_faltas': conteudo_holerite.desconto_faltas,
                'base_fgts': conteudo_holerite.base_fgts, 
                'fgts_mes': conteudo_holerite.fgts_mes,
                'aliquota_inss': conteudo_holerite.aliquota_inss,
                'base_inss': conteudo_holerite.base_inss,
                'desconto_inss': conteudo_holerite.desconto_inss,
                'aliquota_irrf': conteudo_holerite.aliquota_irrf,
                'base_irrf': conteudo_holerite.base_irrf,
                'desconto_irrf': conteudo_holerite.desconto_irrf,
                'total_descontos': conteudo_holerite.total_descontos,
                'total_vencimentos': conteudo_holerite.total_vencimentos,
                'salario_a_receber': conteudo_holerite.salario_a_receber,
    }

    return jsonify(resposta)