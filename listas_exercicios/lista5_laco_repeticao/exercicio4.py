"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Laço de repetição

Exercício 4 DESAFIO

"""

print("\n\nAs 15 primeiras aproximações de Pi são: ")

pi = 3

print(f"\n{pi}")

for x in range(2, 29, 4):

    pi = pi + 4/(x*(x+1)*(x+2))

    print(f"\n{pi}")

    pi = pi - 4/((x+2)*(x+3)*(x+4))

    print(f"\n{pi}")
