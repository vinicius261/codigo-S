"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Bingo - Passo 2

Passo número 2: 
- Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.

"""

import cartela

import sorteios

cartela1 = cartela.gerador_de_cartela()

letra_sorteada, numero_sorteado = sorteios.sorteio_canta_num()

if cartela.verifica_acertos(cartela1, letra_sorteada, numero_sorteado):

    cartela1 = cartela.marca_numero_declara(
        cartela1, letra_sorteada, numero_sorteado, "  ")

else:
    print("\nErrou!\n")

cartela.imprime(cartela1)
