# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math


def problem9(n):
    squares = []
    for c in range(n):
        c_sq = c*c

        for a_sq in squares:
            b_sq = c_sq - a_sq
            if b_sq in squares:
                a = math.sqrt(a_sq)
                b = math.sqrt(b_sq)
                if a + b + c == n:
                    return a*b*c
        squares.append(c_sq)


print(problem9(1000))
