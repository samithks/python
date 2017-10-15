'''Implement the nearest_square function. The function takes an integer argument
limit, and returns the largest square number that is less than limit. A square
number is the product of an integer multiplied by itself, for example 36 is a
square number because it equals 6*6.

You need to do it with out using a loop

'''

#!/usr/bin/python3

import math


def nearest_square(limit):
    '''
    The function takes an integer argument limit, and returns the largest square
    number that is less than limit.
    '''
    # Take the root of this number
    square_root = math.sqrt(limit)
    # Round it down to an integer , let us call it floor_integer
    floor_value = int(square_root)
    # Square the integers
    floor_value_square = floor_value ** 2

    if floor_value_square < limit or floor_value_square == limit:
        return floor_value_square

print nearest_square(50)
