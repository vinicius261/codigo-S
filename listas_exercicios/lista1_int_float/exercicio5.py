"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 1: Tipos Numéricos

Exercício 5

"""

numero = (input("\nInsira um número de 4 dígitos:"))

lst = []

lst.extend(numero)

lst_int = list(map(int,lst))

soma = sum(lst_int)

print(f"\nA soma dos alagrismo do numero {numero} é {soma}")