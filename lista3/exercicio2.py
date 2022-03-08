Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lista de exercícios: Dicionários e Sets

# Exercício 2

dicionario={"AM":"Amazonas", "AC":"Acre", "PB":"Paraíba","MT":"Mato Grosso"}

nome_estado=input(f"Digite a sigla do estado:  ") 

print(f"\nO estado correpondente à sigla é {dicionario[nome_estado]}.")