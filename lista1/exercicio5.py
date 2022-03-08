Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lista de exercícios: Tipos Numéricos

#Exercício 5

numero=(input("\nInsira um número de 4 dígitos: \n"))

list=[]

list.extend(numero)

primeiro_algarismo=int(list[0])

segundo_algarismo=int(list[1])

terceiro_algarismo=int(list[2])

quarto_algarismo=int(list[3])

soma=primeiro_algarismo+segundo_algarismo+terceiro_algarismo+quarto_algarismo

print(f"\nA soma dos alagrismo do numero {numero} é {soma}")