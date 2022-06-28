
from datetime import date
import mysql.connector
from typing import List
from  src.funcionarios import Funcionario
from src.cargos import *


class CadastroFuncionarios():
    def __init__(self) -> None:
        self.__funcionarios: List[Funcionario] = []

    def cadastrar(self, nome:str, cpf:int, data_admissao: date, descr_cargo: str):
        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='codewars')
        cursor = cnx.cursor()

        query = ("INSERT INTO codewars.funcionarios (nome, cpf, data_admissao, cargo)  VALUES (%(nome)s, %(cpf)s, %(data_admissao)s, %(cargo)s)")
       
        cursor.execute(query, {
            "nome": nome,
            "cpf": cpf,
            "data_admissao": data_admissao,
            "cargo": descr_cargo 
        })
        cnx.commit()

        cursor.close()
        cnx.close()

    def consultar(self, matricula: int, alteracao=False) -> Funcionario:

        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='codewars')
        cursor = cnx.cursor()

        query = ("SELECT * FROM codewars.funcionarios WHERE matricula=%s")
        
        cursor.execute(query, [matricula])
        
        for linha in cursor:
            conversor  = CadastroFuncionarios()
            cargo = conversor.convert_json_entrada(linha[4])
            matricula_= str(linha[0]).zfill(6)
            funcionario = Funcionario(matricula_, linha[1], linha[2], linha[3], cargo)
            
        cnx.commit()

        cursor.close()
        cnx.close()
        return funcionario

        # if alteracao == False:
        #     print(f"{funcionario.matricula}\n{funcionario.nome}\n{funcionario.cpf}\n{funcionario.data_admissao}\n{funcionario.cargo.descricao}\n{funcionario.salario_base}\n{funcionario.comissao}\n\n")
        # return funcionario

    def excluir(self, matricula):

        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='codewars')
        cursor = cnx.cursor()

        query = ("DELETE FROM codewars.funcionarios WHERE matricula=%s")

        cursor.execute(query, [matricula])

        cnx.commit()

        cursor.close()
        cnx.close()

    def alterar(self, matricula, dados_escolhidos: dict):

        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='codewars')
        cursor = cnx.cursor()
        
        if "nome" in dados_escolhidos.keys():
            query = ("UPDATE codewars.funcionarios SET nome = %s WHERE matricula=%s")
            cursor.execute(query, [dados_escolhidos["nome"], matricula] ,True )
            cnx.commit()


        if "cpf" in dados_escolhidos.keys():
            query = ("UPDATE codewars.funcionarios SET cpf = %s WHERE matricula=%s")
            cursor.execute(query, [dados_escolhidos["cpf"], matricula], True )
            cnx.commit()


        if "data_admissao" in dados_escolhidos.keys():
            query = ("UPDATE codewars.funcionarios SET data_admissao = %s WHERE matricula=%s")
            cursor.execute(query, [dados_escolhidos["data_admissao"], matricula], True )
            cnx.commit()

        if "cargo" in dados_escolhidos.keys():
            query = ("UPDATE codewars.funcionarios SET cargo = %s WHERE matricula=%s")
            cursor.execute(query, [dados_escolhidos["cargo"], matricula], True )
            cnx.commit()

        cursor.close()
        cnx.close()          

    def listar_todos(self):
        cnx = mysql.connector.connect(user='root', password='123456',
                                      host='127.0.0.1',
                                      database='codewars')
        cursor = cnx.cursor()

        query = ("SELECT * FROM codewars.funcionarios")
        
        cursor.execute(query)

        funcionarios = []

        for linha in cursor:
            conversor  = CadastroFuncionarios()
            cargo = conversor.convert_json_entrada(linha[4])
            matricula_= str(linha[0]).zfill(6)
            funcionario = Funcionario(matricula_, linha[1], linha[2], linha[3], cargo)
            funcionarios.append(funcionario)

        cnx.commit()

        cursor.close()
        cnx.close()
        return funcionarios

    def convert_json_entrada(self, cargo: str) -> Cargos:
        if cargo == 'Cientista de dados':
            return CientistaDeDados

        elif cargo == 'Especialista em Business Intelligence':
            return EspecialistaBusines

        elif cargo == 'Desenvolvedor Mobile Sênior':
            return DesenvolvedorSenior

        elif cargo == 'Desenvolvedor Mobile Pleno':
            return DesenvolvedorPleno
        elif cargo == 'Desenvolvedor Junior':
            return DesenvolvedorJunior

        elif cargo == 'Gerente de Projetos':
            return GerenteDeProjetos

    def convert_json_saida(self, cargo: Cargos) -> str:
        if cargo == CientistaDeDados:
            return 'Cientista de dados'

        elif cargo == EspecialistaBusines:
            return 'Especialista em Business Intelligence'

        elif cargo == DesenvolvedorSenior:
            return 'Desenvolvedor Mobile Sênior'

        elif cargo == DesenvolvedorPleno:
            return 'Desenvolvedor Mobile Pleno'

        elif cargo == DesenvolvedorJunior:
            return 'Desenvolvedor Junior'

        elif cargo == GerenteDeProjetos:
            return 'Gerente de Projetos'

