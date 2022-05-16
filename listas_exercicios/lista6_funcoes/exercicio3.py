"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Funções

Exercício 3

"""


def inversao_de_numero(numero: int) -> str:

    numero_iteravel = str(numero)

    numero_invertivel = []

    numero_invertivel.extend(numero_iteravel)

    numero_invertivel.reverse()

    numero_invertido = " "

    for index in range(len(numero_iteravel)):

        numero_invertido = numero_invertido + str(numero_invertivel[index])

    return numero_invertido


numero = int(input("\n\nDigite um número para obter o seu reverso: "))

numero_invertido = inversao_de_numero(numero)

print(f"\n\nA inversão de {numero} é : {numero_invertido}")
