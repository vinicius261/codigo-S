"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Quadrado Mágico

"""

import magic_square_module

from math import factorial

user_choice = int(input("\nDigite as dimensões do quadrado: "))

rep_control = []

contador = 0

print(
    f"\nOs quadrados mágicos {user_choice}X{user_choice} são: ")

while len(rep_control) != factorial(user_choice**2):

    square_default, sum_lines = magic_square_module.create_square(user_choice)

    if square_default not in rep_control:

        rep_control.append(square_default)

        contador_for = 0

        for n in square_default.values():

            sum_line = sum(n)

            if sum_line == sum_lines:
                contador_for += 1

        for n in range(user_choice):

            column = []

            for n1 in range(user_choice):

                value = square_default[n1][n]

                column.append(value)

            if sum(column) == sum_lines:
                contador_for += 1

        diagonal = []

        for n in range(user_choice):

            value = square_default[n][n]
            diagonal.append(value)

        if sum(diagonal) == sum_lines:
            contador_for += 1

        if contador_for == (2*user_choice)+1:

            # print(f"\nA soma é {sum_lines:.0f} e o quadrado mágico é: \n")

            magic_square_module.print_saquare(square_default, user_choice)

            contador += 1

print(
    f"Número de quadrados mágicos {user_choice}X{user_choice} encontrados : {contador}")
