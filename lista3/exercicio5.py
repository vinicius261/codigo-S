Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lista de exercícios: Dicionários e Sets

# Exercício 5

aluno_nota={"Abel":6,"Balbino":7,"Custódio":2,"Douglas":5}

nota_maxima=max(list(aluno_nota.values()))

nota_minima=min(list(aluno_nota.values()))

print(f"Nota máxima -> {aluno_nota[nota_maxima]}:{nota_maxima}")

print(f"Nota minima -> {aluno_nota[nota_minima]}:{nota_minima}")