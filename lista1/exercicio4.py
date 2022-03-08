Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lista de exercícios: Tipos Numéricos

#Exercício 4

peso_kg=float(input("\nQual é o seu peso em kg?\n"))

altura_m=float(input("\nQual a sua altura em metros? Atenção, use ponto ao invés de vírgula.\n"))

IMC=peso_kg/altura_m**2

print(f"Seu IMC é {IMC:3.1f}")