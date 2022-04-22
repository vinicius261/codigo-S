"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco
Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 16 parece ser mais simples que usar uma matriz 4x4.
Extra: Permita que o usuário indique o tamanho do cubo mágico (2x2, 3x3, 4x4, etc.)
"""

# Sem dicas agora! Tentem elaborar toda a lógica do zero!

from collections import defaultdict

import magic_square_module

from math import factorial

user_choice = int(input("\nDigite as dimensões do quadrado: "))

rep_control = []

for _ in range(factorial(user_choice**2)):

    standard_square = magic_square_module.create_square(user_choice)

    if standard_square not in rep_control:
        
        rep_control.append(standard_square)

        sum_line1 = standard_square[0][0] + standard_square[0][1] + standard_square[0][2] 

        sum_line2 = standard_square[1][0] + standard_square[1][1] + standard_square[1][2] 

        sum_line3 = standard_square[2][0] + standard_square[2][1] + standard_square[2][2] 

        sum_diag =  standard_square[0][0] +  standard_square[1][1] + standard_square[2][2]  

        if sum_line1 == sum_line2 == sum_line3 == sum_diag:

            print(f"\nA soma é {sum_diag} e o quadrado mágico é: \n")

            magic_square_module.print_saquare(standard_square)