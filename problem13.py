# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# (numbers in problem13_data)

from collections import deque
import itertools


def problem13(n):

    data_file = open('problem13_data')

    data = []
    for line in data_file:
        data.append([int(x) for x in line.strip()])
    data_file.close()
    num_rows = len(data)
    num_cols = len(data[0])

    final_sum = deque()
    carryover = 0
    for col in reversed(range(num_cols)):
        col_sum = carryover
        for row in range(num_rows):
            col_sum += data[row][col]
        final_sum.appendleft(col_sum % 10)
        carryover = col_sum / 10

    while carryover != 0:
        final_sum.appendleft(carryover % 10)
        carryover = carryover / 10

    output_as_iter = itertools.islice(final_sum, 0, n)
    output_as_list = [str(x) for x in output_as_iter]
    return ''.join(output_as_list)


print problem13(10)