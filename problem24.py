# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
# 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# So, we know that these permutations must be numerically in order.
# Therefore for example 0123456789 will be before 0123456798.

# That is, switch the last two digits, and work your way to the front.

# That is, find all the permutations of 8 and 9. Then move on to the permutations of 7, 8 and 9. Then permutations of
#  6, 7, 8, and 9. Etc. So we need to add these up until we reach a million. How many permutations are there of a
# single set? There's... six ways to do three, so I think it's 3!. 6 7 8 and 9 would be 4!, then. Let's test it.

# 6 7 8 9
# 6 7 9 8
# 6 8 7 9
# 6 8 9 7
# 6 9 7 8
# 6 9 8 7
# Then same with the 7s and the 8s and 9s. That's 6 * 4, or 24, or 4 * 3 * 2 * 1. So. Assumption validated
# What we want to do... hang on. We know how to find the number of permutations of 10. That's 10!. That isn't hard.
# Question is, when do we get to a million? Well, let's see.


# OK, we get there in the ninth digit. That is, it's somewhere within that, it's a permutation where the second digit
#  has changed. First digit's definitely zero, is all we know from doing that. Damn. So. Specifically which? Well,
# we can do the same exercise for the next number up, if we know the interval.

# Yeah I'm doing this math wrong. There are over 3 million permutations. At what point do we stop, at 1 million? We
# know the first tenth have zero, the second tenth have one, etc. Within that, the first tenth have zero, the second
# tenth have one, etc. "Within that" meaning... within that interval. Meaning how many 362,880s would it take to get
# up to a million? Well, 1 million / 362880. We have that, that's three. So we know that we're on a 2 for the first
# digit. Ok so now we're 300,000*3 = 900,000 of the way there. We still have 100,000 permutations to go. Hang on,
# that isn't right. OK. 362,880 permutations per first number. How many permutations per second number? 362880/9. and
#  per third number is whatever that is divided by eight. so basically, we have to keep dividing: 10, 9,
# 8 in sequence, until we get to a million. do we? 362880 permutations per first number - what does that tell us? It
# tells us that by the time we get to a million, we're three permutations in, so we're at digit 2. that is a million
# divided by 362880. by extension, we get down to dividing by 9 - that's 40320, and we know we've already used up
# 300,000 permutations getting up to digit 2, so now we have how many left?

# No. It's 362880 * 2 = 725,760. That's how many we've done so far. So we have  274,240 left. and we've got 40320
# permutations per second digit, so that's 6 exactly for the second digit. which means the answer is 1602345789
#  36,288,
# right? Right. And how many per third number? What if now this isn't divisible by 10? It has to be, right?
# no. we've just done, just finished all the permutations for the second digit; we haven't got any left. so now we
# start over with the third digit. ugh.


# a b c d e
# how many permutations of b c d e? that's 4*3*2 = 24.
# but ohhh, you divide by four then, don't you? because there are only ... no, it could be a? no, it could only be
# one of four numbers.

# ok. so. we start with 2, because we got through 362880 permutations and then another 362880. now we're on 2. and
# we've got how many to go? we've got 274240 to go. and now instead of having nine different numbers to permute,
# we now have eight ones. that's 40320 permutations. so let's think about it. we do this six times. we go through 0.
# then 1. then 2. then 3. then 4. as soon as we get done with all the 5s, we're completely done with a million. so
# it's the very last 5. or is it the very first 6?

# let's do it mathematically. 9! is what we start with. then we take a million divided by that number. y is going to
# be our first digit. so we'll multiply it by 10 to the 9. that's y. then we have r. we want to take r divided by 8!.
#  good now we do it again.

# 2598764310

import math
# x = math.factorial(9)
# (y, r) = divmod(1000000, x)
# y *= 10**9
# (a, b) = divmod(r, math.factorial(8))
# y += (a * 10**8)
# (c, d) = divmod(b, math.factorial(7))
# y += (c * 10**7)
# print(y)

# so here's what we do. this is the part we know is repeating.

result = 0
permutations_left = 1000000
digits = []
for i in range(9, -1, -1):

    if permutations_left == 0:
        digit = next(d for d in range(10) if d not in digits)
        result += digit * 10**i
        digits.append(digit)
        continue

    permutations_this_level = math.factorial(i)

    # print('{} {}'.format(permutations_this_level, permutations_left))
    print('Dividing {} by {}.'.format(permutations_left, permutations_this_level))
    (count_revs, permutations_left) = divmod(permutations_left, permutations_this_level)
    print('Result: {} with remainder {}.'.format(count_revs, permutations_left))

    # need to COUNT UP FROM ZERO, skipping all of the items in the list but still counting up "digit" times
    digit = 0
    for counter in range(count_revs):
        while digit in digits:
            digit += 1
        digit += 1
    while digit in digits:
        digit += 1

    result += digit * 10**i
    digits.append(digit)
    print(digits)
    print(permutations_left)

print(result)

# Fuck, you can't repeat digits.
# OK, what does that mean? It means we do not have what we thought we did. we've got 10! permutations, but at the
# next level, now that we know there's two, there are only 9 digits to work with... hang on. so 6 is fine,
# but the next level digit has to be something else. which means we'll have more left over. let's try just making it
# something else. but it CAN'T be. fuck.

# why was I assuming that we want to get up to the max iterations? what if we stopped at zero? we'd have more
# iterations to get through in the rest of the thing, but we could do that. the problem is that 9! is less than a
# million and 10! is more than a million. and we're going in order. so we are trying to find the millionth. and the
# millionth will be when we've churned through all the iterations in order. so ok. we're churning through em. what
# happens as we churn? we start with first digit as 0, second as 1, then 2 3 4 5 6 7 8 9. when we have to switch the
# first digit to 1, that's when we now have only 9 digits to work with. so the second digit has got to be something
# in the range of 0 through 9 but without the 1. that is, we have to skip the 1. that's ok. let's try that.

# damn so we skipped whatever digits had previously been chosen... but that didn't work. let's check how many
# permutations we have left at each stage.