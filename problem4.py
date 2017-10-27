# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from time import time


def is_palindrome(n):
    s = str(n)

    r = len(s) / 2
    if len(s) % 2 == 1:
        r += 1

    for i in range(0, r):
        if s[i] != s[i*-1 - 1]:
            return False

    return True


# brute-force it...
def problem4():
    palindromes = []
    found = False
    for i in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            if is_palindrome(i*j):
                palindromes.append(i*j)

    return max(palindromes)


# still brute-force it? but in a different way I guess?
def problem4_v2():
    for i in reversed(range(10000, 1000000)):
        if is_palindrome(i):
            for j in reversed(range(100, 1000)):
                if i % j == 0:
                    k = i / j
                    if len(str(k)) == 3:
                        return i
    return None


# iterate only through palindromes
def problem4_v3():

    # try six-digit palindromes
    for i in reversed(range(100, 1000)):
        s = str(i) + str(i)[::-1]
        n = int(s)

        for j in reversed(range(100, 1000)):
            if n % j == 0:
                k = n / j
                if k >= 100 and k < 1000:
                    return n

    # if that didn't work, move on to five-digit palindromes
    for i in reversed(range(100, 1000)):
        s = str(i) + str(i)[1::-1]
        n = int(s)

        for j in reversed(range(100, 1000)):
            if n % j == 0:
                k = n / j
                if k >= 100 and k < 1000:
                    print n


# function to make palindromes using only numerical operations
def make_palindrome(x, odd_length=False):

    reversed_x = 0

    if odd_length:
        x_copy = x / 10
    else:
        x_copy = x

    num_digits = 0
    while x_copy > 0:
        num_digits += 1
        reversed_x = (reversed_x * 10) + (x_copy % 10)
        x_copy /= 10

    return x * 10**num_digits + reversed_x


# iterate only through palindromes, without string manipulation (fastest)
def problem4_v4():

    palindromes = []
    # try six-digit palindromes
    for i in reversed(range(100, 1000)):
        n = make_palindrome(i, False)
        palindromes.append(n)

        for j in reversed(range(100, 1000)):
            if n % j == 0:
                k = n / j
                if k >= 100 and k < 1000:
                    return n

    # if that didn't work, move on to five-digit palindromes
    for p in palindromes:
        n = p % 10000 / 10
        for j in reversed(range(100, 1000)):
            if n % j == 0:
                k = n / j
                if k >= 100 and k < 1000:
                    print n

start = time()
v1 = problem4()
end = time()
print "v1 retrieved answer {} in {} seconds".format(v1, end - start)

start = time()
v2 = problem4_v2()
end = time()
print "v2 retrieved answer {} in {} seconds".format(v2, end - start)

start = time()
v3 = problem4_v3()
end = time()
print "v3 retrieved answer {} in {} seconds".format(v3, end - start)

start = time()
v4 = problem4_v4()
end = time()
print "v4 retrieved answer {} in {} seconds".format(v4, end - start)
