"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Progamação Orientada a Objetos

Exercício 2.1 - Outras maneira de fazer

"""


class Roman:
    def __init__(self, roman: str) -> None:
        self.roman = roman

    def convert_int(self) -> int:
        roman = self.roman
        roman_list = list(roman)
        roman_values = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                        "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        inte = []
        two_letters_list = ["Z"]
        for letter in roman_list:
            two_letter = two_letters_list[-1] + letter
            possible_two_letters = ["CM", "XC", "XL", "IX", "IV"]
            if two_letter in possible_two_letters:
                letter = two_letter
                inte.pop(-1)
            inte.append(roman_values[letter])
            two_letters_list.append(letter)
        integeer = sum(inte)

        return integeer


roman = Roman("MCMXLIX")

integeer = roman.convert_int()

print(integeer)
