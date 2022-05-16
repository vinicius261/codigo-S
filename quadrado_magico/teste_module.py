"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Quadrado Mágico

"""


from collections import defaultdict
import itertools


from random import shuffle



def create_square(numero: int) -> defaultdict:
    """Cria um candidato a quadrado mágico"""
    
    numbers = list(range(1, (numero**2)+1))

    
    for number in range(0, len(numbers)+1):
        for combination in itertools.combinations(numbers, number):
            if len(combination) == len(numbers):
                numbers = list(combination)


    # shuffle(numbers)

    lines_sum = sum(numbers)/numero

    lines = defaultdict()

    for n in range(numero):

        new_numbers = []

        for _ in range(numero):

            new = numbers.pop()

            new_numbers.append(new)

        lines[n] = new_numbers

    return lines, lines_sum


def print_saquare(square: defaultdict, number: int) -> None:

    for num in range(number):

        line = ' '.join([str(value).zfill(2) for value in square[num]])

        print(line)
    print(f"\n")
