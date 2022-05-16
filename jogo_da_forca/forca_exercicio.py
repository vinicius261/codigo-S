"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Jogo da Forca

"""
import modulo_forca

print("Jogo da Forca!")

secret_word = modulo_forca.get_secret_word()

forca_limpa = []

for _ in secret_word:
    forca_limpa.append("_")

print(f"\n{forca_limpa}")

contador = 1

for _ in range((len(secret_word) + 6)):

    palpite = input("\n\nChute a letra: ")

    letras_ja_escolhidas = []

    while palpite not in modulo_forca.CONTROLE and palpite in letras_ja_escolhidas:
        palpite = input("\n\nChute apenas letras: ")

    secret_word_loop = list(secret_word)

    letras_ja_escolhidas.append(palpite)

    if palpite.upper() in secret_word_loop:
        while palpite.upper() in secret_word_loop:
            index = secret_word_loop.index(palpite.upper())
            forca_limpa.pop(index)
            forca_limpa.insert(index, palpite.upper())
            secret_word_loop[index] = 0
    else:
        print(modulo_forca.STATUS[contador])
        if contador == 6:
            print(f"\nNão foi dessa vez. A palavra era {secret_word}")
            break
        contador += 1

    print(f"\n{forca_limpa}")

    if forca_limpa == secret_word:
        print("\nParabéns!")
        break
