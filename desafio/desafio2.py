#Lista de exercícios: Desafio -Jogo em que o úsuario tenta advinhar a soma de dois dados lançados.

#Exercício 2

from random import uniform

condicao = "Sim".upper()

while condicao == "Sim".upper() or condicao == "S".upper():
    dado1 = uniform(1, 6)

    dado2 = uniform(1, 6)

    dado1_int = round(dado1)

    dado2_int = round(dado2)

    soma_dos_dados = dado1_int + dado2_int

    validacao_do_insert = list(range(2, 13))

    numero_usuario = int(input("\nInsira seu palpite para a soma dos números virados nos dados: "))

    while numero_usuario not in validacao_do_insert:
        numero_usuario = int(input("\nEssa soma não é possível. \nOs números de cada dado vão de 1 a 6.\nPor favor, tente novamente: "))

    if numero_usuario != soma_dos_dados:
        
        print(f"Você errou. A soma dos dados é {soma_dos_dados}. O valor do primeiro dado é {dado1_int} e o do segundo é {dado2_int}.")

    else :
        print(f"Parabéns! Você acertou a soma dos dados! O valor do primeiro dado é {dado1_int} e o do segundo é {dado2_int}. ")

    condicao = input("\nDeseja jogar novamente? ").upper()
