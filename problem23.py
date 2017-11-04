# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
# two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
# written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
# this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from problem21 import sum_divisors


def inside_loop(i, abundants):
    result = set()
    for a in abundants:
        if i+a >= 28124:
            return result
        result.add(i+a)
    return result


i = 12
abundants = [i]
sums_of_two = {i*2}


while True:
    i += 1
    if i >= 28112:  # 28112:
        break
    if sum_divisors(i) <= i:
        continue
    abundants.append(i)
    sums_of_two = sums_of_two | inside_loop(i, abundants)
    # print(i)  # debug

sum_of_sums_of_two = sum(sums_of_two)
all_numbers = 28123 * 28124 / 2
print(all_numbers - sum_of_sums_of_two)