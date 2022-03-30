#Lista de exercícios: Laço de repetição

#Exercício 6

#Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.

N = int(input("Digite o valor de N: "))

H = 1

for numero in range(2, N):

    H = H + 1/numero
    
print(f" O valor de H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N para N = {N} é {H}")    