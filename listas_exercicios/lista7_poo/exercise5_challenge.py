"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Progamação Orientada a Objetos

Exercício 5 DESAFIO

"""


class Bird:
    def __init__(self, altura_maxima_de_voo, nao_voa=False) -> None:
        self.altura_maxima_de_voo = altura_maxima_de_voo
        self.nao_voa = nao_voa
        pass

    def calcula_velocidade(self):
        pass

    def c():
        pass


class European(Bird):
    def __init__(self, altura_maxima_de_voo, nao_voa) -> None:
        super().__init__(altura_maxima_de_voo, nao_voa)

    def calcula_velocidade_base(self):
        velocidade = ...
        return velocidade

    def calcula_velocidade(self):
        return self.calcula_velocidade_base()


class African(Bird):
    def __init__(self, altura_maxima_de_voo, nao_voa) -> None:
        super().__init__(altura_maxima_de_voo, nao_voa)

    def calcula_fator_carga(self):
        pass

    def calcula_velocidade(self):
        velocidade = self.c() - self.calcula_fator_carga() * self.altura_maxima_de_voo
        return velocidade


class Norway(Bird):
    def __init__(self, altura_maxima_de_voo, nao_voa) -> None:
        super().__init__(altura_maxima_de_voo, nao_voa)

    def calcula_velocidade(self):
        if self. nao_voa == True:
            velocidade = 0
            return velocidade
        else:
            self.c()
