"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Laço de repetição

Exercício 3

"""

criancas_0_2 = 0

criancas_3_12 = 14

visitantes_13_64 = 23

idosos_65 = 18

valores_ingressos = []


idade_inserida = int(input(
    "\n\nDigite a idade dos visitantes uma de cada vez. \n\nQuando não houver mais novas idades pressione apenas 'Enter'.\n\nInsira a idade: "))

if idade_inserida < 3:
    valores_ingressos.append(criancas_0_2)

elif 2 < idade_inserida < 13:
    valores_ingressos.append(criancas_3_12)

elif 13 < idade_inserida < 65:
    valores_ingressos.append(visitantes_13_64)

elif 64 < idade_inserida:
    valores_ingressos.append(idosos_65)

while idade_inserida != '':
    idade_inserida = input(
        "\nDigite a proxima idade ou 'Enter' para encerrar: ")

    if idade_inserida == '':
        break

    idade_int = int(idade_inserida)

    if idade_int < 3:
        valores_ingressos.append(criancas_0_2)

    elif 2 < idade_int < 13:
        valores_ingressos.append(criancas_3_12)

    elif 13 < idade_int < 65:
        valores_ingressos.append(visitantes_13_64)

    elif 64 < idade_int:
        valores_ingressos.append(idosos_65)

custo_total = sum(valores_ingressos)

print(
    f"\n\nO valor total para admissão do grupo no zoológico é R${custo_total:3.2f}\n\n")
