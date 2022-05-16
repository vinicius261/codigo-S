"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 4: Condicionais

Exercício 5

"""

placa_veiculo = input("\n Insira a placa do veículo: ")

placa_lista = []

placa_lista.extend(placa_veiculo)

letras = placa_lista[0]+placa_lista[1]+placa_lista[2]

numeros = placa_lista[4]+placa_lista[5]+placa_lista[6]+placa_lista[7]


if len(placa_lista) == 8 and placa_lista[3] == "-" and letras.isalpha() and numeros.isalnum() and letras.isupper():
    print("\n True\n")

else:
    print("\n False\n")
