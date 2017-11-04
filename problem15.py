# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly
# 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20x20 grid?
import itertools

# Looked online - instead you could do a binomial expansion by constructing Pascal's triangle!!

# both of these solutions are too inefficient - they freeze up the computer. But the answer is just 40 choose 20


def problem15(n):
    path = [0] * (2*n)
    return len([x for x in itertools.combinations(path, n)])


def num_paths(n):
    # n by n grid
    paths = [0, 1]
    for step in range(n*2 - 1):
        paths_copy = paths[:]
        for path_index, num_rights in enumerate(paths_copy):
            if num_rights < n:
                paths[path_index] = num_rights + 1  # move to the right
                if step - num_rights + 1 < n:
                    paths.append(num_rights)  # add a new path which moves down
        print(step, paths)
    return len(paths)
