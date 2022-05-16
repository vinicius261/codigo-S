"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 2: Listas

Exercício 1

"""

variavel = 1 +5 +8

dicionario = {"Vinicius": "SP"}

lista = ["string", 8, variavel, ["Python", dicionario["Vinicius"], 12], not True]

for elemento in lista:
    print(f"\nElemento {elemento} na posição {lista.index(elemento)} ")

print(lista[2])    