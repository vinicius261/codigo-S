"""
How Bootcamps - Stone - /código[s]
Data: 24/03/2022
Autor: Henrique Junqueira Branco
Enunciado: BINGO do zero!
Uma cartela de BINGO consiste em 5 colunas de 5 números que são rotulados com as letras B, I, N, G e O.
Atenção: Google it, para quem nunca viu uma cartela dessas!
Existem 15 números que podem aparecer sob cada letra respeitando a regra abaixo.
- B -> números variando de 1 a 15  (inclusos)
- I -> números variando de 16 a 30 (inclusos)
- N -> números variando de 31 a 45 (inclusos)
- ... e assim por diante
Passo número 0:
- Escreva uma função que crie uma cartela de BINGO aleatória. Dica(podemos usar um dicionário!). 
- As chaves serão as letras B, I, N, G e O. 
- Os valores serão as listas de cinco números aleatórios respeitando a regra dos intervalos de cada letra. 
Passo número 1: 
- Escreva uma segunda função que exiba a cartela de BINGO com as colunas rotuladas apropriadamente
- Formate a saída no terminal para que a cartela seja impressa em forma de colunas (letras e seus valores abaixo)
Passo número 2: 
- Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.
Passo número 3:
- Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
- Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.
Passo número desafio:
- Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
    * O número mínimo de sorteio para que a carteja seja vencedora (não necessariamente preencher toda a cartela!)
    * A média do número de sorteios para que a carteja seja vencedora
    * O número máximo de sorteios para que a cartela seja vencedora
"""

import cartela

import sorteios

import cartela_fixa

num_de_rodadas = []

num_sorteios = int(input("Digite o quantidade de sorteios para o teste:")) 

for _ in range(num_sorteios):

    cartela2 = cartela_fixa.gerador_de_cartela_fixa()

    num_sorteados = [0]

    num_possiveis = list(range(1,76))

    cartela_ganhou = False

    contador = 0

    num_da_vez = 0

    while num_sorteados not in num_possiveis and cartela_ganhou==False and contador <= 1000:

        contador = contador + 1

        while num_da_vez in num_sorteados:

            letra_da_vez, num_da_vez = sorteios.sorteio()

        num_sorteados.append(num_da_vez)


        if cartela.verifica_acertos(cartela2, letra_da_vez, num_da_vez):

            cartela2 = cartela.marca_numero(cartela2, letra_da_vez, num_da_vez, "  ")

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