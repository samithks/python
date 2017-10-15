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
    # Round it down to an integer , let us call it floor_integer and then add 1
    # to this integer to get the ceil_integer
    floor_value = int(square_root)
    ceil_value = floor_value + 1
    # Square both of those integers
    floor_value_square = floor_value ** 2
    ceil_value_square = ceil_value ** 2
    # Calculate which square is the closest one to the original number n and
    # then return it
    floor_distance = limit - floor_value_square
    ceil_distance = ceil_value_square - limit
    if floor_distance < ceil_distance:
        return floor_value_square
    else:
        return ceil_value_square


print nearest_square(30)
