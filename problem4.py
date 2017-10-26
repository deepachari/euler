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

# 10*10, 10*9, 9*9, 10*8, 9*8, 8*8, 8*7... 10*8


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
    for i in reversed(range(100, 1000)):
        s = str(i) + str(i)[::-1]
        n = int(s)

        for j in reversed(range(100, 1000)):
            if n % j == 0:
                k = n / j
                if k >= 100 and k < 1000:
                    return n

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