# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
# hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British
# usage.


digits_w = ['one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine']

teens_w = ['ten',
           'eleven',
           'twelve',
           'thirteen',
           'fourteen',
           'fifteen',
           'sixteen',
           'seventeen',
           'eighteen',
           'nineteen']

decades_w = ['twenty',
             'thirty',
             'forty',
             'fifty',
             'sixty',
             'seventy',
             'eighty',
             'ninety']

digits = [len(word) for word in digits_w]
teens = [len(word) for word in teens_w]
decades = [len(word) for word in decades_w]

result = 0
result += sum(digits)
result += sum(teens)

decades_digits = []
for decade in decades:
    decades_digits.append(decade)
    result += decade
    for digit in digits:
        result += decade + digit
        decades_digits.append(decade + digit)

hundred = len('hundred')
hundred_and = len('hundredand')
for digit1 in digits:
    result += digit1 + hundred
    for digit2 in digits:
        result += digit1 + hundred_and + digit2
    for teen in teens:
        result += digit1 + hundred_and + teen
    for d_d in decades_digits:
        result += digit1 + hundred_and + d_d

result += len('onethousand')

print result