import math


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt = math.sqrt(sq)
    if sqrt.is_integer():
        return (sqrt + 1) ** 2

    return -1
