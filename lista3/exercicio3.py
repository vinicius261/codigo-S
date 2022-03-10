 #Lista de exercícios: Dicionários e Sets

# Exercício 3

from ast import Num


dicionario = {"Abel":15,"Balbino":67,"Custódio":26,"Douglas":54}

dicionario_ordenado = sorted(dicionario.items(), key=lambda dicionario:dicionario[1], reverse=True)

print(dicionario_ordenado)