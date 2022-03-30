import cartela

from random import choice, randint

from collections import defaultdict

def sorteio ():

    letra_sorteada = choice(cartela.LETRAS)

    minimo, maximo = cartela.min_max(letra_sorteada)

    numero_sorteado = randint(minimo, maximo)

    return letra_sorteada, numero_sorteado

def sorteio_canta_num ():

    letra_sorteada = choice(cartela.LETRAS)

    minimo, maximo = cartela.min_max(letra_sorteada)

    numero_sorteado = randint(minimo, maximo)

    print(f"\nA combinação sorteada foi: {letra_sorteada} / {numero_sorteado}")

    return letra_sorteada, numero_sorteado

