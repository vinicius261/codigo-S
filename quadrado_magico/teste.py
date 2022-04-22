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

import magic_square_module

from math import factorial

user_choice = int(input("\nDigite as dimensões do quadrado: "))

rep_control = []

contador = 0

numero_de_sorteados = 0

while len(rep_control) != factorial(user_choice**2):

    square_default, sum_lines = magic_square_module.create_square(user_choice)

    numero_de_sorteados += 1

    print(numero_de_sorteados)
    
    if square_default not in rep_control:
        
        rep_control.append(square_default)

        contador_for = 0

        for n in square_default.values() :

            sum_line = sum(n)
            
            if sum_line == sum_lines:
                contador_for +=1

        for n in range(user_choice):
            
            column = []

            for n1 in range(user_choice):

                value = square_default[n1][n]
                
                column.append(value)

            if sum(column) == sum_lines:
                contador_for +=1

        diagonal = []        

        for n in range(user_choice):
        
            value = square_default[n][n]
            diagonal.append(value)

        if sum(diagonal) == sum_lines:
            contador_for +=1

             
        
        if contador_for == (2*user_choice)+1:

            print(f"\nA soma é {sum_lines:.0f} e o quadrado mágico é: \n")

            magic_square_module.print_saquare(square_default, user_choice)

            break

            contador += 1

            print(f"Número de quadrados mágicos {user_choice}X{user_choice} encontrados : {contador}")