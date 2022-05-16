"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 3: Dicionários e Sets

Exercício 4

"""

dicionario = {1: "vermelho", 2: "azul", 3: "marrom"}

for chave, valor in dicionario.items():

    dicionario[chave] = len(valor)

print(dicionario)
