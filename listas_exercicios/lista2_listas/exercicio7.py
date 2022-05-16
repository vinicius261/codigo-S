"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 2: Listas

Exercício 7

"""

from ast import Str


lista = ["1","7","99", "15"]

lista[0] = int(lista[0])

lista[1] = int(lista[1])

lista[2] = int(lista[2])

lista[3] = int(lista[3])

print(f"A conversão dos objetos da lista para inteiros fica: {lista}")

lista[0] = str(lista[0])

lista[1] = str(lista[1])

lista[2] = str(lista[2])

lista[3] = str(lista[3])

print(f"A conversão dos objetos da lista para string fica: {lista}")


sigla_estado = {"SP" : "São Paulo", "MG" : "Minas Gerais"}

print(f"\nTransformando as chaves em um outro objeto: {sigla_estado.keys()}")

print(f"\nTransformando as chaves em uma lista: {list(sigla_estado)}")



check_sp = "SP" in sigla_estado
print(f"\nA sigla SP está nas chaves? Resposta: {check_sp}")