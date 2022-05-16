"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 1: Tipos Numéricos

Exercício 1

"""

numeroA = int(input("\nDigite um número inteiro: "))

numeroB = int(input("\nDigite outro número inteiro: "))

soma = numeroA + numeroB

diferenca_B_A = numeroB - numeroA

produto_A_B = numeroA * numeroB

quociente_A_B = numeroA // numeroB

resto_A_B = numeroA % numeroB

from math import log10
log_10_A = log10(numeroA)

A_elevado_B = numeroA ** numeroB

print(f"\nA soma dos números é: {soma}\n")

print(f"A diferença B-A={diferenca_B_A}\n")

print(f"A multiplicação dos números é: {produto_A_B}\n")

print(f"O quociente da divisão de A por B é: {quociente_A_B}\n")

print(f"O resto da divisão de A por B é: {resto_A_B}\n")

print(f"O log10 de A é: {log_10_A}\n")