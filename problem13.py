# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# (numbers in problem13_data)

data_file = open('problem13_data')
data = []
for line in data_file:
    print type(line)
    for c in line:
        print "rijfdsa {}".format(c)
    data.append([int(x) for x in line.split(' ')])
data_file.close()

sums = []
num_rows = len(data)
num_cols = len(data[0])

for col in reversed(range(num_cols)):
    s = 0
    for row in range(num_rows):
        s += data[row][col]
