

from datetime import date
from  src.cargos import CientistaDeDados, DesenvolvedorJunior, DesenvolvedorPleno, DesenvolvedorSenior, EspecialistaBusines, GerenteDeProjetos
from src.funcionarios import Funcionario
import src.cadastro


class Holerite():
    def __init__(self, funcionario: Funcionario) -> None:
        self.funcionario = funcionario

    def gerar_holerite(self, mes, faltas):
        ano = date.today()
        # mes = input("\nPara qual mês quer gerar o holerite?")
        # faltas = int(input(
        #     f"\nQuantas faltas tem o funcionário {self.funcionario.nome}?"))
        
        base_fgts,  fgts_mes = self.calcula_FGTS()
        base_inss, desconto_inss, aliquota_inss = self.calcula_desconto_INSS()
        base_irrf, desconto_irrf, aliquota_irrf = self.calcula_IRRF(
            desconto_inss)
        desconto_faltas = (self.funcionario.salario_base/30)*faltas
        total_descontos = desconto_inss + desconto_irrf

        total_vencimentos = self.funcionario.salario_base + self.funcionario.comissao

        salario_a_receber = total_vencimentos - total_descontos

        self.imprime_holerite(ano,mes, fgts_mes, base_fgts, base_inss, desconto_inss, base_irrf, desconto_irrf, desconto_faltas,
                              total_descontos, total_vencimentos, salario_a_receber, faltas, aliquota_irrf, aliquota_inss)

        return (ano,mes, fgts_mes, base_fgts, base_inss, desconto_inss, base_irrf, desconto_irrf, desconto_faltas,
                              total_descontos, total_vencimentos, salario_a_receber, faltas, aliquota_irrf, aliquota_inss)
                              
    def gerar_todos_holerites(self, cadastro: src.cadastro.CadastroFuncionarios):
        mes = input("\nPara qual mês quer gerar os holerites?")

        for funcionario in cadastro.__funcionarios:
            self.funcionario = funcionario

            base_fgts,  fgts_mes = self.calcula_FGTS()
            base_inss, desconto_inss, aliquota_inss = self.calcula_desconto_INSS()
            base_irrf, desconto_irrf, aliquota_irrf = self.calcula_IRRF(
                desconto_inss)
            total_descontos = desconto_inss + desconto_irrf

            total_vencimentos = self.funcionario.salario_base + self.funcionario.comissao

            salario_a_receber = total_vencimentos - total_descontos

    def calcula_desconto_INSS(self) -> float:
        base_calc_inss = self.funcionario.salario_base + self.funcionario.comissao

        if 1212.01 < base_calc_inss <= 2427.35:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            
            desconto_INSS = desconto_faixa1 + desconto_faixa2 
            aliquota = "9%"
                
        elif 2427.36 < base_calc_inss <= 3641.03:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            deconto_faixa3 = (base_calc_inss - 2427.36) * 0.12

            desconto_INSS = desconto_faixa1 + desconto_faixa2 + deconto_faixa3
            aliquota = "12%"

        elif 3641.04 < base_calc_inss <= 7087.22:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            deconto_faixa3 = (3641.04 - 2427.35) * 0.12
            desconto_faixa4 = (base_calc_inss - 3641.04) * 0.14

            desconto_INSS = desconto_faixa1 + desconto_faixa2 + \
                deconto_faixa3 + desconto_faixa4
            aliquota = "14%"

        elif 7087.23 <= base_calc_inss:
            desconto_faixa1 = 1212*0.075
            desconto_faixa2 = (2427.35 - 1212) * 0.09
            deconto_faixa3 = (3641.04 - 2427.35) * 0.12
            desconto_faixa4 = (7087.22 - 3641.04) * 0.14

            desconto_INSS = desconto_faixa1 + desconto_faixa2 + \
                deconto_faixa3 + desconto_faixa4
            aliquota = "14%"   

        return base_calc_inss, desconto_INSS, aliquota

    def calcula_IRRF(self, desconto_INSS) -> float:
        base_calc_irrf = self.funcionario.salario_base + \
            self.funcionario.comissao - desconto_INSS

        if 1903.89 <= base_calc_irrf <= 2826.65:
            desconto_IRRF = (base_calc_irrf*0.075) - 142.8
            aliquota = "7,5%"

        elif 2826.66 <= base_calc_irrf <= 3751.05:
            desconto_IRRF = (base_calc_irrf*0.15) - 354.8
            aliquota = "15%"

        elif 3751.06 <= base_calc_irrf <= 4664.68:
            desconto_IRRF = (base_calc_irrf*0.225) - 636.13
            aliquota = "22,5%"

        elif 4664.69 <= base_calc_irrf:
            desconto_IRRF = (base_calc_irrf*0.275) - 869.36
            aliquota = "27,5%"

        return base_calc_irrf, desconto_IRRF, aliquota

    def calcula_FGTS(self) -> float:
        base_calc_fgts = self.funcionario.cargo.salario_base + self.funcionario.comissao
        fgts_mes = base_calc_fgts*0.08
        return base_calc_fgts, fgts_mes

    def comissao_holerite(self) -> str:
        if self.funcionario.cargo.__eq__(CientistaDeDados):
            comissao = "10%"
            return comissao

        elif self.funcionario.cargo.__eq__(EspecialistaBusines):
            comissao = "8%"
            return comissao

        elif self.funcionario.cargo.__eq__(DesenvolvedorSenior):
            comissao = "7%"
            return comissao

        elif self.funcionario.cargo.__eq__(DesenvolvedorPleno):
            comissao = "3%"
            return comissao

        elif self.funcionario.cargo.__eq__(DesenvolvedorJunior):
            comissao = "10%"
            return comissao

        elif self.funcionario.cargo.__eq__(GerenteDeProjetos):
            comissao = "8%"
            return comissao

    def imprime_holerite(self, ano, mes, fgts_mes, b_fgts, b_inss, desc_inss, b_irrf, desc_irrf, desc_faltas, desc_total, venc_total, salario_receber, faltas, aliq_irrf, aliq_inss) -> str:
        comissao = self.comissao_holerite()

        print(f"=============================================================================================\n\
Empresa XPTO Alimentos                                          Recibo de Pagamento de Salário\n\
Endereço: Rua XV de Novembro, 15, Centro                        \
Mês de referência: {mes}/{ano.year}                          \n\
CNPJ: 12.345.678/0001-00\n\
==============================================================================================    ")

        print(f"Matricula       Nome                          Data de admissão    Função\n\
{self.funcionario.matricula}          {self.funcionario.nome}        {self.funcionario.data_admissao}          {self.funcionario.cargo.descricao}\n\
\
==============================================================================================")

        print(f"Código          Descrição                     Referência          Proventos       Descontos\n\
101             Salário Base                  22,50               R${self.funcionario.salario_base}      \n\
203             Comissão                      {comissao}                 R${self.funcionario.comissao}      \n\
303             Faltas                        {faltas}                                   R${desc_faltas}      \n\
973             INSS folha                    {aliq_inss}                                 R${desc_inss}      \n\
978             IRRF folha                    {aliq_irrf}                                 R${desc_irrf}      \n\
==============================================================================================")

        print(f"                                                        Total vencimentos     Total descontos\n\
                                                        R${venc_total}                R${desc_total}\n\
Salário base |Base INSS |Base FGTS |FGTS do mês |Base IRRF                    Liquido a receber\n\
R${self.funcionario.salario_base}   R${b_inss}   R${b_fgts}     R${fgts_mes}      R${b_irrf}              R${salario_receber}\n\
==============================================================================================")


