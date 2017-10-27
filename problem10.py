# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# array with each index being a bit indicating whether the index is a prime or not


# gets all primes up to but not including max_num
class PrimeFinder:

    def __init__(self, max_num):
        self.max_num = max_num
        self.base = [True] * self.max_num
        self.base[1] = False
        self.base[::2] = [False] * ((self.max_num + 1) / 2)
        self.base[2] = True
        self.get_primes()

    @property
    def primes_list(self):
        return [n for n, is_prime in enumerate(self.base) if is_prime]

    @property
    def prime_sum(self):
        return sum(self.primes_list)

    def get_primes(self):
        # iterate through all the potential primes
        for i in xrange(3, self.max_num, 2):
            if not self.base[i]:
                continue
            self.mark_multiples(i)

    def mark_multiples(self, prime):
        self.base[prime * 2::prime] = [False] * ((self.max_num - prime - 1) / prime)


pf = PrimeFinder(2000000)
for prime in pf.primes_list:
    print prime
print pf.prime_sum