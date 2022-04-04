from collections import defaultdict

from random import randint, seed

from cartela import min_max

LETRAS = ("B", "I", "N","G", "O")

def gerador_de_cartela_fixa() -> defaultdict[str, list[int]] :

    """Gera uma mesma cartela com 5 números para cada letra."""
    
    seed(14)

    cartela = defaultdict(list)

    for letra in LETRAS: 

        minimo, maximo = min_max(letra)

        while len(cartela[letra]) < 5:
            num_aleatorio = randint(minimo, maximo)
            
            if num_aleatorio in cartela[letra] :
                continue

            cartela[letra].append(num_aleatorio)

            cartela[letra].sort()

    return cartela    