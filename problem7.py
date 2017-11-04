# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

primes = [2, 3]


def problem7(x):

    if x == 2:
        return x

    candidate = 3
    for index in range(3, x + 1):
        candidate += 2
        while not is_prime(candidate):
            candidate += 2
        primes.append(candidate)
    return candidate


def is_prime(n):

    for p in primes:
        if n % p == 0:
            return False

    return True


print(problem7(10001))
