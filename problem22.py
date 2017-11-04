# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
#
# What is the total of all the name scores in the file?


def problem22(filename):

    data = open(filename)
    names = data.readline().strip('"').split('","') #[:3]
    names.sort()
    score_sum = 0
    offset = ord('A') - 1

    for index, name in enumerate(names):
        name_value = sum([ord(c) - offset for c in name])
        score_sum += name_value * (index + 1)
        # print index+1, name, [ord(c) - offset for c in name], name_value, score_sum

    return score_sum


print(problem22('problem22_data'))
