# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# brute force
def found(x):
    for i in range(1, 20):
        if x % i != 0:
            return False

    return True

result = 40
while not found(result):
    result += 20

print(result)
