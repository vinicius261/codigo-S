"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Funções

Exercício 2

"""

from xmlrpc.client import boolean


def triangulo_criterios(lado1: float, lado2: float, lado3: float) -> boolean:
    """Verifica se as medidas dos lados possibilitam a formação de um triângulo."""
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        return False
    elif lado1 + lado2 <= lado3 or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
        return False
    else:
        return True


Lado1 = float(input("Insira o primeiro lado do triângulo: "))

Lado2 = float(input("Insira o segundo lado do triângulo: "))

Lado3 = float(input("Insira o terceiro lado do triângulo: "))

verificacao_triangulo = triangulo_criterios(Lado1, Lado2, Lado3)

if verificacao_triangulo == True:
    print("Esses lados podem formar um triângulo.")

else:
    print("Esses lados não podem formar um triângulo.")
