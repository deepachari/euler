# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable
# numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def sum_divisors(x):
    result = 0
    for i in range(1, x//2+1):
        if x % i == 0:
            result += i
    return result


def problem21(n):

    result = set()
    sums_of_divisors = {}
    for i in range(1, n):
        if i not in sums_of_divisors:
            sums_of_divisors[i] = sum_divisors(i)
        s1 = sums_of_divisors[i]

        if i == s1:
            continue

        if s1 not in sums_of_divisors:
            sums_of_divisors[s1] = sum_divisors(s1)
        s2 = sums_of_divisors[s1]

        if i == s2:
            result.add(i)
            result.add(s2)

    return sum(result)


#print(problem21(10000))