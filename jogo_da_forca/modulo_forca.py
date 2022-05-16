"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Jogo da Forca

"""

import string

from random import choice

CONTROLE = list(string.ascii_lowercase + string.ascii_uppercase)


def get_secret_word() -> list():
    """Devolve uma palavra aleatória de uma lista."""

    recebe_arquivo = open("letras.txt", "r")

    arquivo = recebe_arquivo.read().split(",")

    lista_palavras = []

    for palavra in arquivo:

        palavra = palavra.lstrip()

        lista_palavras.append(palavra)

    for palavra in lista_palavras:

        for letra in palavra:

            index = lista_palavras.index(palavra)

            if letra not in CONTROLE:
                lista_palavras[index] = "-"
                break

    for palavra in lista_palavras:
        if "-" in lista_palavras:
            lista_palavras.remove("-")

    palavra_sorteada = choice(lista_palavras)

    palavra_sorteada = palavra_sorteada.upper()

    palavra_sorteada_indexavel = []

    palavra_sorteada_indexavel.extend(palavra_sorteada)

    return palavra_sorteada_indexavel


STATUS = [
    r"""
_____________
|            |
|            
|           
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|            |
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|\
|           
|=====================
""",
    r"""
_____________
|            |
|            O
|           /|\
|           / 
|=====================
""",
    r"""
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
''''''''''|_`-' `-' |'''|
|'|'''''''\ \       ''|'|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
VOCÊ PERDEU, NOOB!
""",
]
