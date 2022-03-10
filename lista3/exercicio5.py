#Lista de exercícios: Dicionários e Sets

# Exercício 5

aluno_nota={"Abel":6,"Balbino":7,"Custódio":2,"Douglas":5}

nota_maxima=max(list(aluno_nota.values()))

nota_minima=min(list(aluno_nota.values()))

lista_aluno=list(aluno_nota.keys())

lista_notas=list(aluno_nota.values())

posicao_nota_max=lista_notas.index(nota_maxima)

posicao_nota_min=lista_notas.index(nota_minima)

nome_max=lista_aluno[posicao_nota_max]

nome_min=lista_aluno[posicao_nota_min]

print(f"Nota máxima -> {nome_max}:{nota_maxima}")

print(f"Nota minima -> {nome_min}:{nota_minima}")

print(type(nota_maxima))