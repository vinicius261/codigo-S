#Lista de exercícios: Laço de repetição

#Exercício 1

numeros_usuario = []

numero_inserido = float(input("\nAdicone o primeiro número para o cáculo da média: "))

while numero_inserido == 0:
    numero_inserido = float(input("O primeiro número inserido deve ser diferente de 0, digite novamente:"))
    
numeros_usuario.append(numero_inserido)

while 0 not in numeros_usuario:
    numero_inserido = float(input("\nAdicione mais um ou digite 0 para indicar que não há mais números para inserir: "))
    
    numeros_usuario.append(numero_inserido)


media = sum(numeros_usuario)/ len(numeros_usuario)    

print (f"\nA média do números inseridos é {media}.")
