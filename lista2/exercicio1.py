Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Lista de exercícios: Listas

# Exercício 1

variavel=1+5+8

dicionario={"Vinicius": "SP"}

lista = ["string", 8, variavel, ["Python", dicionario["Vinicius"], 12], not True]

#Uso do list.index() redundante, apenas para gravar o método

print(f"\nElemento {lista[0]} na posição {lista.index(lista[0])} ")

print(f"\nElemento {lista[1]} na posição {lista.index(lista[1])} ")

print(f"\nElemento {lista[2]} na posição {lista.index(lista[2])} ")

print(f"\nElemento {lista[3]} na posição {lista.index(lista[3])} ")

print(f"\nElemento {lista[4]} na posição {lista.index(lista[4])} ")