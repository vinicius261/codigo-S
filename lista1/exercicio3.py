 #Lista de exercícios: Tipos Numéricos

#Exercício 3


lado1=float(input("\nDigite os 3 lados do triangulo:\nLado 1: "))

lado2=float(input("\nLado 2: "))

lado3=float(input("\nLado 3: "))

variavel_auxiliar=(lado1+lado2+lado3)/2

area_triangulo=(variavel_auxiliar*(variavel_auxiliar-lado1)*(variavel_auxiliar-lado2)*(variavel_auxiliar-lado3))**(1/2)

print(f"A área do triângulo é: {area_triangulo} ")