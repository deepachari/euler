# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date, timedelta


def date_generator(start, end):
  while start <= end:
    yield start
    start += timedelta(days=1)


def problem19(start, end):
    num_sundays = 0
    for d in date_generator(start, end):
        if d.day == 1 and d.weekday() == 6:
            num_sundays += 1

    return num_sundays


start = date(year=1901, month=1, day=1)
end = date(year=2000, month=12, day=31)
print(problem19(start, end))
