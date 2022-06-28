from abc import ABC

 
class Cargos(ABC):
    def __init__(self) -> None:
        self.__codigo = None
        self.__descricao = None
        self.__salario_base = None
        self.__comissao = None

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


class CientistaDeDados(Cargos):
    def __init__(self) -> None:
        super().__init__()
        self.__codigo = 10
        self.__descricao = "Cientista de dados"
        self.__salario_base = 10200
        self.__comissao = 0.1*self.__salario_base

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


class EspecialistaBusines(Cargos):
    def __init__(self) -> None:
        super().__init__()
        self.__codigo = 20
        self.__descricao = "Especialista em Business Intelligence"
        self.__salario_base = 7000
        self.__comissao = 0.08*self.__salario_base

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


class DesenvolvedorSenior(Cargos):
    def __init__(self) -> None:
        super().__init__()
        self.__codigo = 30
        self.__descricao = "Desenvolvedor Mobile Sênior"
        self.__salario_base = 6700
        self.__comissao = 0.07*self.__salario_base

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


class DesenvolvedorPleno(Cargos):
    def __init__(self) -> None:
        super().__init__()
        self.__codigo = 31
        self.__descricao = "Desenvolvedor Mobile Pleno"
        self.__salario_base = 3550
        self.__comissao = 0.06*self.__salario_base

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


class DesenvolvedorJunior(Cargos):
    def __init__(self) -> None:
        super().__init__()
        self.__codigo = 32
        self.__descricao = "Desenvolvedor Junior"
        self.__salario_base = 3000
        self.__comissao = 0.03*self.__salario_base

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


class GerenteDeProjetos(Cargos):
    def __init__(self) -> None:
        super().__init__()
        self.__codigo = 50
        self.__descricao = "Gerente de Projetos"
        self.__salario_base = 8900
        self.__comissao = 0.08*self.__salario_base

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao


# vini = GerenteDeProjetos()

# vini.salario_base = 10000

# print(vini.salario_base)
