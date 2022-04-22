class Convert_roman_inte:
    def __init__(self, roman :str) -> None:
        self.roman = roman    
       
    def convert(self) -> int:
        roman = self.roman
        roman_list = list(roman)
        roman_values = { "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I":1}
        inte = []
        letter_duo_list = ["T"]
        for letter in roman_list:
            letter_duo =  letter_duo_list[-1] + letter 
            duo_letters = ["CM", "XC", "XL", "IX", "IV"]
            if letter_duo in duo_letters:
                letter = letter_duo
                inte.pop(-1)
            inte.append(roman_values[letter])
            letter_duo_list.append(letter)
        integeer = sum(inte)

        return integeer

integeer = Convert_roman_inte("MCMXLIX")

print(integeer.convert())
    




