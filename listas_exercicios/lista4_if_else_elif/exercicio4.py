"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 4: Condicionais

Exercício 4

"""

ano = int(input("\nInsira um ano para saber se ele é bissexto: "))


if (ano % 400) == 0:
    print(f"\nO ano {ano} é bissexto.")

elif (ano % 100) == 0:
    print(f"\nO ano {ano} não é bissexto.")

elif (ano % 4) == 0:
    print(f"\nO ano {ano} é bissexto.")

else:
    print(f"\nO ano {ano} não é bissexto.")
