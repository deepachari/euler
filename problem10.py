# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def problem10(n):

    # array with each index being a bit indicating whether the index is a prime or not
    base = [True] * (n+1)
    base[0] = False
    base[1] = False
    base[2] = True
    base[4::2] = [False] * ((n - 2) / 2)

    # iterate through all the potential primes
    for i in xrange(3, len(base), 2):
        if not base[i]:
            continue
        base[i*2::i] = [False] * ((n - i) / i)
        print i

    return sum(i for i, b in enumerate(base) if b)


print problem10(2000000)