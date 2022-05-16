"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Laço de repetição

Exercício 6

"""

N = int(input("Digite o valor de N: "))

H = 1

for numero in range(2, N):

    H = H + 1/numero

print(f" O valor de H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N para N = {N} é {H}")
