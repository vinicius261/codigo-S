"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Bingo

"""
from collections import defaultdict
from random import randint

LETRAS = ("B", "I", "N", "G", "O")


def min_max(letra: str) -> tuple[int]:
    """Gera os limites mínimo e máximo dos números para a letra.

    Agrs:
        letra(str)

    Returns:
        tuple[int]: minimo, maximo
    """

    intervalo = {"B": (1, 15), "I": (16, 30), "N": (
        31, 45), "G": (46, 60), "O": (61, 75)}

    minimo, maximo = intervalo[letra][0], intervalo[letra][1]

    return minimo, maximo


def gerador_de_cartela() -> defaultdict[str, list[int]]:
    """Gera uma cartela com 5 números para cada letra."""

    cartela = defaultdict(list)

    for letra in LETRAS:

        minimo, maximo = min_max(letra)

        while len(cartela[letra]) < 5:
            num_aleatorio = randint(minimo, maximo)

            if num_aleatorio in cartela[letra]:
                continue

            cartela[letra].append(num_aleatorio)

            cartela[letra].sort()

    return cartela


def imprime(cartela: dict[str, list[int]]) -> None:
    """Imprime uma cartela formatada.

    Args:
        cartela (dict[str, list[int]]): cartela de entrada
    """

    print("B  I  N   G  O")

    for linha in range(5):

        elementos = " ".join([str(elemento[linha]).zfill(2)
                             for elemento in cartela.values()])

        print(elementos)


def marca_numero(cartela: defaultdict, letra: str, numero: int, caracter: str):
    """Marca os números sortedos presentes na cartela fornecida."""

    indice = cartela[letra].index(numero)

    cartela[letra][indice] = caracter

    return cartela


def marca_numero_declara(cartela: defaultdict, letra: str, numero: int, caracter: str):
    """Marca e apresenta os números sortedos presentes na cartela fornecida."""

    indice = cartela[letra].index(numero)

    cartela[letra][indice] = caracter

    print(f"\nAcertou o número {numero}!\n")

    return cartela


def verifica_acertos(cartela: defaultdict, letra: str, numero: int):
    """Verifica se o número fornecido existe na cartela fornecida."""
    if numero in cartela[letra]:
        return True

    return False
