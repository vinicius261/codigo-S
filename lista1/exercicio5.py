 #Lista de exercícios: Tipos Numéricos

#Exercício 5

numero = (input("\nInsira um número de 4 dígitos: \n"))

lst = []

lst.extend(numero)

# primeiro_algarismo = int(lst[0])

# segundo_algarismo = int(lst[1])

# terceiro_algarismo = int(lst[2])

# quarto_algarismo = int(lst[3])

# soma = primeiro_algarismo+segundo_algarismo+terceiro_algarismo+quarto_algarismo

lst_int = list(map(int,lst))

soma = sum(lst_int)

print(f"\nA soma dos alagrismo do numero {numero} é {soma}")