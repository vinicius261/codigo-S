"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 2: Listas

Exercício 4

"""
temperaturas = {"Janeiro": 0, "Fevreiro": 0, "Março": 0, "Abril": 0, "Maio": 0,
                "Junho": 0, "Julho": 0, "Agosto": 0, "Setembro": 0, "Outubro": 0,
                "Novembro": 0, "Dezembro": 0}

for mes in temperaturas.keys():

    temperaturas[mes] = int(input(f"Digite a temperatura média de {mes}: "))

temperatura_media_anual = sum(temperaturas.values())/len(temperaturas.values())

print(
    f"\n\n A temperatura média anual é {temperatura_media_anual:2.1f} e os meses que superaram essa marca são: ")

for mes, temperatura in temperaturas.items():
    if temperatura > temperatura_media_anual:
        print(f"\n {mes} - {temperatura}")
