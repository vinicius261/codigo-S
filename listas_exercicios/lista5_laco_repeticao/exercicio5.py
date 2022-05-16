"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Laço de repetição

Exercício 5

"""

nome_atleta = input("\n\nDigite o nome do atleta: ")

notas_input = input(
    "\n\nDigite as 7 notas em sequência, separadas por vírgula e sem espaços: ")

notas_todas = notas_input.split(",")

notas_todas_ordenadas = sorted(notas_todas)

nota_min = notas_todas_ordenadas[0]

nota_max = notas_todas_ordenadas[6]

notas_todas_ordenadas.pop(0)

notas_todas_ordenadas.pop()

notas_int = list(map(float, notas_todas_ordenadas))

media = sum(notas_int)/len(notas_int)

print(
    f"\n\nAtleta: {nome_atleta}\nMelhor nota: {nota_max}\nPior nota: {nota_min}\nMédia: {media}")
