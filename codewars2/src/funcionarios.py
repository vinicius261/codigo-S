import src.cargos


class Funcionario():
    def __init__(self, matricula: int, nome: str, cpf: int, data_admissao: str, cargo: src.cargos.Cargos) -> None:
        self.__matricula = matricula
        self.__nome = nome
        self.__cpf = cpf
        self.__data_admissao = data_admissao
        self.__cargo = cargo 
        self.__salario_base = self.cargo.salario_base
        self.__comissao = self.cargo.comissao

    @property
    def matricula(self):
        return self.__matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def data_admissao(self):
        return self.__data_admissao

    @data_admissao.setter
    def data_admissao(self, value):
        self.__data_admissao = value

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, value):
        self.__cargo = value

    @property
    def salario_base(self):
        return self.cargo.salario_base

    @property
    def comissao(self):
        return self.cargo.comissao
