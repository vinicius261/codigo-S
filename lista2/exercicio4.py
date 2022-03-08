Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Exercício 4

janeiro=int(input("Digite a temperatura média de Janeiro: "))

fevreiro=int(input("Digite a temperatura média de Fevereiro: "))

março=int(input("Digite a temperatura média de Março: "))

abril=int(input("Digite a temperatura média de Abril: "))

maio=int(input("Digite a temperatura média de Maio: "))

junho=int(input("Digite a temperatura média de Junho: "))

julho=int(input("Digite a temperatura média de Julho: "))

agosto=int(input("Digite a temperatura média de Agosto: "))

setembro=int(input("Digite a temperatura média de Setembro: "))

outubro=int(input("Digite a temperatura média de Outubro: "))

novembro=int(input("Digite a temperatura média de Novembro: "))

dezembro=int(input("Digite a temperatura média de Dezembro: "))

temperaturas=[janeiro,fevreiro,março,abril, maio,junho,julho,agosto,setembro,outubro,novembro,dezembro] 

temperatura_media_anual=sum(temperaturas)/len(temperaturas)

print(f"\n\n A temperatura média anual é {temperatura_media_anual:2.1f} e os meses que superaram essa marca são: ")

if temperaturas[0]>temperatura_media_anual:
    print(f"\n Janeiro - {temperaturas[0]}")
if temperaturas[1]>temperatura_media_anual:
    print(f" Fevereiro - {temperaturas[1]}")
if temperaturas[2]>temperatura_media_anual:
    print(f" Março - {temperaturas[2]}")    
if temperaturas[3]>temperatura_media_anual:
    print(f" Abril - {temperaturas[3]}")
if temperaturas[4]>temperatura_media_anual:
    print(f" Maio - {temperaturas[4]}")
if temperaturas[5]>temperatura_media_anual:
    print(f" Junho - {temperaturas[5]}")
if temperaturas[6]>temperatura_media_anual:
    print(f" Julho - {temperaturas[6]}")
if temperaturas[7]>temperatura_media_anual:
    print(f" Agosto - {temperaturas[7]}")
if temperaturas[8]>temperatura_media_anual:
    print(f" Setembro - {temperaturas[8]}")
if temperaturas[9]>temperatura_media_anual:
    print(f" Outubro - {temperaturas[9]}")
if temperaturas[10]>temperatura_media_anual:
    print(f" Novembro - {temperaturas[10]}")
if temperaturas[11]>temperatura_media_anual:
    print(f" Dezembro - {temperaturas[11]}")        