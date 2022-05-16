"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Funções

Exercício 1

"""


def taximetro(km: int) -> float:
    """Calcula o preço de uma corrida de taxi no país X"""
    return round(4 + km/0.14*0.25, 2)


km_rodados = int(input("Digite a distâcia do seu destino em Km: "))

preco_gasolina = 3

fator_desgaste = 0.55

carro_particular = (preco_gasolina + fator_desgaste) * km_rodados

taxi = taximetro(km_rodados)

transporte_publico = 4.4

print(
    f"A sua viagem vai custar: \nR${carro_particular} de carro paticular \nR${taxi} de táxi \nR${transporte_publico} de transporte público")
