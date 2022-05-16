"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Bingo - Passo 3

Passo número 3:
- Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
- Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.

"""

import cartela

import sorteios

cartela1 = cartela.gerador_de_cartela()

condicao = False

contador = 0

numeros_acertados = []

while condicao == False and contador < 50:

    contador = contador + 1

    letra_sorteada, numero_sorteado = sorteios.sorteio()

    if cartela.verifica_acertos(cartela1, letra_sorteada, numero_sorteado):

        cartela1 = cartela.marca_numero(
            cartela1, letra_sorteada, numero_sorteado, "  ")

        numeros_acertados.append(numero_sorteado)

    for letra in "BINGO":

        if cartela1[letra] == ["  ", "  ", "  ", "  ", "  "]:

            print(
                f"\nA cartela foi vecendora fechando coluna(s) em {contador} rodadas.\nE os números acertados foram {numeros_acertados}.\n")
            condicao = True

    for numero_linha in range(5):

        linha = []

        linha.append(cartela1["B"][numero_linha])

        linha.append(cartela1["I"][numero_linha])

        linha.append(cartela1["N"][numero_linha])

        linha.append(cartela1["G"][numero_linha])

        linha.append(cartela1["O"][numero_linha])

        if linha == ["  ", "  ", "  ", "  ", "  "]:

            print(
                f"\nA cartela foi vecendora fechando linha(s) em {contador} rodadas.\nE os números acertados foram {numeros_acertados}.\n")
            condicao = True


if condicao != True:
    print(f"\nA cartela não ganhou dentro das 50 rodadas. E os números acertados foram {numeros_acertados}.\n\n")

cartela.imprime(cartela1)
