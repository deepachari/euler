# 2**(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**(1000)?

from time import time


def problem16(base, exp):

    product = [1]
    for i in range(1, exp+1):
        multiply(product, base)

    return sum(product)


def multiply(l, n):
    carryover = 0

    for i in range(len(l) - 1, -1, -1):
        digit = l[i] * 2 + carryover
        (carryover, l[i]) = divmod(digit, 10)

    while carryover != 0:
        (carryover, r) = divmod(carryover, 10)
        l.insert(0, r)


def problem16_v2(base, exp):
    product = base**exp
    result = 0
    while product != 0:
        (product, r) = divmod(product, 10)
        result += r
    return result


start = time()
print(problem16(2, 1000))
end = time()
print("v1 - {} seconds".format(end - start))

start = time()
print(problem16_v2(2, 1000))
end = time()
print("v2 - {} seconds".format(end - start))
