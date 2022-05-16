"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 1: Tipos Numéricos

Exercício 4

"""

peso_kg = float(input("\nQual é o seu peso em kg?\n"))

altura_m = float(input("\nQual a sua altura em metros? Atenção, use ponto ao invés de vírgula.\n"))

IMC = peso_kg/altura_m**2

print(f"Seu IMC é {IMC:3.1f}")