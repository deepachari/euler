# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
# 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math
from itertools import permutations
from time import time


def iter_to_num(l):
    result = 0
    mult = 1
    for d in reversed(l):
        result += d * mult
        mult *= 10

    return result


def problem24_v1(n):

    permutations_left = n-1
    digits = []
    for i in range(9, -1, -1):

        permutations_this_level = math.factorial(i)
        (count_revs, permutations_left) = divmod(permutations_left, permutations_this_level)

        # count up from zero "digit" times, skipping all of the items already in the list
        digit = 0
        for counter in range(count_revs):
            while digit in digits:
                digit += 1
            digit += 1
            while digit in digits:
                digit += 1

        digits.append(digit)

    return iter_to_num(digits)


# give the nth permutation of list l
def problem24_v2(l, n):
    return iter_to_num(sorted(permutations(l))[n-1])


# give the nth permutation of list l as a list
def nth_permutation(l, n):

    if not l:
        return l

    permutations_this_level = math.factorial(len(l)-1)
    i, n = divmod(n, permutations_this_level)
    digit = l.pop(i)

    return [digit] + nth_permutation(l, n)


# give the nth permutation of list l
def problem24_v3(l, n):
    return iter_to_num(nth_permutation(sorted(l), n-1))


start = time()
v1 = problem24_v1(1000000)
end = time()
print('v1 found result {} in {} seconds'.format(v1, end-start))
start = time()
v2 = problem24_v2(iter(range(10)), 1000000)
end = time()
print('v2 found result {} in {} seconds'.format(v2, end-start))
start = time()
v3 = problem24_v3(list(range(10)), 1000000)
end = time()
print ('v3 found result {} in {} seconds'.format(v3, end-start))
