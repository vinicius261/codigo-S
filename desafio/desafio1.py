#Lista de exercícios: Desafio - - Jogo em que o usuário tenta adivinhar números sorteados de 1 a 100 
#no menor número de tentavivas possível.

#Exercício 1


from random import randint

numero_de_tentativas = 0

condicao = "Sim".upper()

while condicao == "Sim".upper() :


    numero_sorteado = randint(1,100)

    numeros_validos = list(range(1,101))

    numero_escolhido = int(input("Digite seu palpite para o número sorteado entre 1 e 100 : "))

    numeros_ja_escolhidos = []

    while numero_escolhido not in numeros_validos: 
        numero_escolhido = int(input("O número está entre 1 e 100, digite novamente : "))

    
    while numero_sorteado != numero_escolhido :

        #Incrementado contra a reperição de números
        if  numero_escolhido in numeros_ja_escolhidos :
        
            numero_escolhido = int(input("\nVocê já escolheu esse número digite outro: "))

            while numero_escolhido not in numeros_validos: 
                 numero_escolhido = int(input("O número está entre 1 e 100, digite novamente : "))


        elif numero_escolhido < numero_sorteado :
            
            numeros_ja_escolhidos.append(numero_escolhido)

            numero_de_tentativas = numero_de_tentativas + 1

            numero_escolhido = int(input("\nO número sorteado é maior.Tente novamente: "))

            while numero_escolhido not in numeros_validos: 
                 numero_escolhido = int(input("O número está entre 1 e 100, digite novamente : "))

            
        elif numero_escolhido > numero_sorteado :

            numeros_ja_escolhidos.append(numero_escolhido)

            numero_de_tentativas = numero_de_tentativas + 1

            numero_escolhido = int(input("\nO número sorteado é menor.Tente novamente: "))

            while numero_escolhido not in numeros_validos: 
                numero_escolhido = int(input("O número está entre 1 e 100, digite novamente : "))

    if   numero_sorteado == numero_escolhido:

        numero_de_tentativas = numero_de_tentativas + 1

        print (f"\nParabéns! Você acertou o número sorteado e o número de tentativas foi : {numero_de_tentativas}\n") 

        #zerar a lista de números escolhidos em caso continuidade do jogo.
        numeros_ja_escolhidos = [] 

        #zerar número de tentativas em caso de continuidade do jogo.
        numero_de_tentativas = 0

        condicao = input("Deseja jogar novamente? Responda Sim ou Nao: ").upper()  
 



   


      