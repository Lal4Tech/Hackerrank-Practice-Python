#!/bin/python3

import calendar

def is_leap(year):
    # solution 1
    return calendar.isleap(year)
    # solution 2
    # return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    

if __name__ = '__main__':
    year = int(input())
    print(is_leap(year))


