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

cartela1 = cartela.gerador_de_cartela()

condicao = False

contador = 0

numeros_acertados = []

while condicao == False  and contador < 50:

    contador = contador + 1

    letra_sorteada, numero_sorteado = sorteios.sorteio()

    
    if cartela.verifica_acertos(cartela1, letra_sorteada, numero_sorteado):
        
        cartela1 = cartela.marca_numero(cartela1, letra_sorteada, numero_sorteado, "  ")

        numeros_acertados.append(numero_sorteado)

    for letra in "BINGO":
        
        if cartela1[letra] == [ "  ", "  ", "  ", "  ", "  "]:

            print(f"\nA cartela foi vecendora fechando coluna(s) em {contador} rodadas.\nE os números acertados foram {numeros_acertados}.\n")
            condicao = True
            
            
    for numero_linha in range(5):    
            
        linha = []

        linha.append(cartela1["B"][numero_linha])

        linha.append(cartela1["I"][numero_linha])

        linha.append(cartela1["N"][numero_linha])

        linha.append(cartela1["G"][numero_linha])

        linha.append(cartela1["O"][numero_linha])

                                    

        if linha == ["  ", "  ", "  ", "  ", "  "]:

            print(f"\nA cartela foi vecendora fechando linha(s) em {contador} rodadas.\nE os números acertados foram {numeros_acertados}.\n")
            condicao = True
            

                
if condicao != True :
    print("\nA cartela não ganhou dentro das 50 rodadas.\n")    

cartela.imprime(cartela1)