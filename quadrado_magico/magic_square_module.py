
from collections import defaultdict

from random import shuffle

def create_square (numero : int) -> defaultdict:
    """Cria um candidato a quadrado mágico"""
    numbers = list(range(1, (numero**2)+1))

    shuffle(numbers)

    lines_sum = sum(numbers)/numero

    lines = defaultdict()

    for n in range(numero):

        new_numbers = []
    
        for _ in range(numero):

            new = numbers.pop()

            new_numbers.append(new)

        lines[n] = new_numbers

    return lines, lines_sum

def print_saquare (square : defaultdict, number: int) -> None :    
    
    for num in range(number):    
    
        line = ' '.join([str(value).zfill(2) for value in square[num]])

        print(line)
    print(f"\n")