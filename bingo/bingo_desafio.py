"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Bingo -  Parte Desafio

Passo número desafio:
- Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
    * O número mínimo de sorteio para que a carteja seja vencedora (não necessariamente preencher toda a cartela!)
    * A média do número de sorteios para que a carteja seja vencedora
    * O número máximo de sorteios para que a cartela seja vencedora

"""

import cartela

import sorteios

num_de_rodadas = []

num_sorteios = int(input("Digite o quantidade de sorteios para o teste:"))

for _ in range(num_sorteios):

    cartela2 = cartela.gerador_de_cartela()

    num_sorteados = [0]

    num_possiveis = list(range(1, 76))

    cartela_ganhou = False

    contador = 0

    num_da_vez = 0

    while num_sorteados not in num_possiveis and cartela_ganhou == False and contador <= 1000:

        contador = contador + 1

        while num_da_vez in num_sorteados:

            letra_da_vez, num_da_vez = sorteios.sorteio()

        num_sorteados.append(num_da_vez)

        if cartela.verifica_acertos(cartela2, letra_da_vez, num_da_vez):

            cartela2 = cartela.marca_numero(
                cartela2, letra_da_vez, num_da_vez, "  ")

        for letra in "BINGO":

            if cartela2[letra] == ["  ", "  ", "  ", "  ", "  "]:

                # print(f"A cartela foi vecendora fechando coluna(s) e com {contador} rodadas\n")
                cartela_ganhou = True

        for numero_linha in range(5):

            linha = []

            linha.append(cartela2["B"][numero_linha])

            linha.append(cartela2["I"][numero_linha])

            linha.append(cartela2["N"][numero_linha])

            linha.append(cartela2["G"][numero_linha])

            linha.append(cartela2["O"][numero_linha])

            if linha == ["  ", "  ", "  ", "  ", "  "]:

                # print(f"A cartela foi vecendora fechando linha(s) e com {contador} rodadas.\n")
                cartela_ganhou = True

    # cartela.imprime(cartela2)

    num_de_rodadas.append(contador)

min_rodadas = min(num_de_rodadas)

max_rodadas = max(num_de_rodadas)

media_rodadas = sum(num_de_rodadas)/len(num_de_rodadas)

print(f"\n\nDentro de {num_sorteios} rodadas os números mímino, máximo e média de rodadas para completar a cartelas foram:\nMIN = {min_rodadas}\nMAX = {max_rodadas}\nMEDIA = {media_rodadas}")
