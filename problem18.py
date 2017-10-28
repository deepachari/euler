# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:

# [triangle in problem18_data]

data_file = open('problem18_data')
data = []
for line in data_file:
    line_list = [int(n) for n in line.strip().split()]
    data.append(line_list)
data_file.close()

sums = [[[data[0][0]]]]

for r in range(len(data) - 1):
    sums.append([])
    this_row = sums[0]
    next_row = sums[1]
    for i in range(len(data[r]) + 1):
        next_row.append([])
    for c in range(len(data[r])):
        left_child = data[r + 1][c]
        right_child = data[r + 1][c + 1]
        sums_so_far = this_row[c]
        next_row[c].extend([s + left_child for s in sums_so_far])
        next_row[c+1].extend([s + right_child for s in sums_so_far])
    sums.pop(0)

print max([x for sublist in sums[-1] for x in sublist])