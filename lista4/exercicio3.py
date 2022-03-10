 #Lista de exercícios: Condicionais
 
# Exercício 3


valores_definidos = {"Britadeira": 130, "Cortador de grama": 106, "Despertador": 70,"Comodo em silêncio": 40}

decibelimetro = int(input("\nInsira o valor indicado pelo decibelímetro: "))

tipo_som_indexavel = list(valores_definidos.keys())

valor_do_tipo_de_som_indexavel = list(valores_definidos.values())

if decibelimetro in valores_definidos.values():
    index = valor_do_tipo_de_som_indexavel.index(decibelimetro)
    print(f"\nEsse som é do(a) {tipo_som_indexavel[index]}")

elif   valor_do_tipo_de_som_indexavel[1] < decibelimetro < valor_do_tipo_de_som_indexavel[0]:
   
    print(f"\nEsse som está entre {tipo_som_indexavel[1]} e {tipo_som_indexavel[0]} ")

elif   valor_do_tipo_de_som_indexavel[2] < decibelimetro < valor_do_tipo_de_som_indexavel[1]:
   
    print(f"\nEsse som está entre {tipo_som_indexavel[2]} e {tipo_som_indexavel[1]} ")   

elif   valor_do_tipo_de_som_indexavel[3] < decibelimetro < valor_do_tipo_de_som_indexavel[2]:
   
    print(f"\nEsse som está entre {tipo_som_indexavel[3]} e {tipo_som_indexavel[2]} ")     

else:
    print("\nEsse valor está fora dos valores mínimos e máximos.")
 
