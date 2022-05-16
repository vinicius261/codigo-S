"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Lista de exercícios 5: Progamação Orientada a Objetos

Exercício 1

"""


class Convert_int_roman:
    def __init__(self, inte: int):
        self.inte = inte

    def convertion(self) -> str:
        thousand = self.inte//1000
        remainder = self.inte % 1000
        nine_hundred = remainder//900
        if remainder >= 900:
            remainder = remainder % 900
        five_hundred = remainder//500
        if remainder >= 500:
            remainder = remainder % 500
        four_hundred = remainder//400
        if remainder >= 400:
            remainder = remainder % 400
        hundred = (remainder % 400)//100
        if remainder >= 100:
            remainder = remainder % 100
        ninety = (remainder % 100)//90
        if remainder >= 90:
            remainder = remainder % 90
        fifty = (remainder % 90)//50
        if remainder >= 50:
            remainder = remainder % 50
        fourty = (remainder % 50)//40
        if remainder >= 40:
            remainder = remainder % 40
        ten = (remainder % 40)//10
        if remainder >= 10:
            remainder = remainder % 10
        nine = (remainder % 10)//9
        if remainder >= 9:
            remainder = remainder % 9
        five = (remainder % 9)//5
        if remainder >= 5:
            remainder = remainder % 5
        four = (remainder % 5)//4
        if remainder >= 4:
            remainder = remainder % 4
        one = (remainder % 4)//1

        roman = thousand*"M"+nine_hundred*"CM"+five_hundred*"D"+four_hundred*"CD"+hundred * \
            "C"+ninety*"XC"+fifty*"L"+fourty*"XL" + ten * \
            "X"+nine*"IX"+five*"V"+four*"IV"+one*"I"

        return roman


inteiro = Convert_int_roman(349)

print(inteiro.convertion())
