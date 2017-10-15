'''Implement the nearest_square function. The function takes an integer argument
limit, and returns the nearest square number that is less than limit.

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
    # calculate the decimal part of the root
    decimal_of_root = square_root - int(square_root)
    print decimal_of_root
    # Compare this decimal part to 0.5. In case it is lower than 0.5, consider
    # the square of floor integer of the root. Otherwise, ceil the root and then
    # square it.
    if decimal_of_root < 0.5:
        return int(square_root) ** 2
    else:
        return (int(square_root) + 1) ** 2


print nearest_square(35)
