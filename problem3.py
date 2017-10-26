# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# had to consult online for this one
# every number can be expressed as 2^[something] * 3^[something] * 5^[something]... etc
# so divide by 2 as many times as you can, then by 3 as many times as possible, then by 5... etc

x = 600851475143
start = 2
while True:
    while x % start == 0 and x != 1:
        x = x/start

    if x == 1:
        break

    if start == 2:
        start += 1
    else:
        start += 2

print start

# def largest_prime_factor(n):
#     largest_factor = 1
#
#     # remove any factors of 2 first
#     while n % 2 == 0:
#         largest_factor = 2
#         n = n / 2
#
#     # now look at odd factors
#     p = 3
#     while n != 1:
#         while n % p == 0:
#             largest_factor = p
#             n = n / p
#         p += 2
#
#     return largest_factor




# this works, but exceeds max recursion depth
# def largest_prime_factor(x, start=2):
#
#     while x % start == 0 and x != 1:
#         x = x/start
#
#     if x == 1:
#         return start
#     else:
#         return largest_prime_factor(x, start+1)



# works, but too inefficient
# def largest_prime_factor(x):
#
#     lpf = math.floor(x / 2)
#     while x % lpf != 0:
#         lpf -= 1
#
#     if lpf == 1:
#         return x
#     else:
#         return largest_prime_factor(lpf)


# print largest_prime_factor(505)

# latest_prime_factor = 3
# prime_factors = [1, 2]
# nonprime_odd_factors = [3]
# i = 1
# while True:
#
#     prime_factors.append(latest_prime_factor)
#     for item in nonprime_odd_factors:
#         nonprime_odd_factors.append(item * latest_prime_factor)
#
#     while nonprime_odd_factors[i] == latest_prime_factor:
#         i += 1
#         latest_prime_factor += 2
#
#     while True:
#         latest_prime_factor += 2
#         if latest_prime_factor not in not_prime_factors:
#             break
#
# print prime_factors[-1]