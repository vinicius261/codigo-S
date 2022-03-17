#Lista de exercícios: Laço de repetição

#Exercício 2

celsius = list(range(0, 101, 10))

print("\n\n-------------------------------------------")
print("-   - Celsius -   -   -   - Fahrenheit-   -")
     
for temperatura in celsius :
    print(f"-   - {temperatura} -   -   -   -   -   - {9/5*temperatura+32}-   -")

print("--------------------------------------------\n\n")    