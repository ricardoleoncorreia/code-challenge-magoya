import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    # Count valleys
    not_ends_at_sea_level = True
    level = 0
    valleys_number = 0
    while not_ends_at_sea_level:
        for step in s:
            previous_level = level
            level += 1 if step == 'U' else -1
            if previous_level == 0 and level < 0:
                valleys_number += 1
        if level:
            print('\nThe path supplied is not valid because it does not end at sea level')
            s = input('Path description (string with "U" and "D"): ')
        else:
            not_ends_at_sea_level = False
    return valleys_number

if __name__ == '__main__':
    fptr = open('counting-valleys-output.txt', 'w')

    n = int(input('Number of steps (must be an even number between 2 and 1,000,000): '))

    # Checking constrains
    while n % 2 == 1 or n < 2 or n > 1000000:
        print('\nThe number of steps must be even to return to sea level')
        n = int(input('Number of steps (must be an even number between 2 and 1,000,000): '))

    s = input('Path description (string with "U" and "D"): ')

    # Checking constrains
    while set(s) != {'D', 'U'} or len(s) != n:
        print('\nPath length must be {} and it must contain only "D" and "U"'.format(n))
        s = input('Path description (string with "U" and "D"): ')

    result = countingValleys(n, s)

    fptr.write('For n={} and s={}, the result: {} valley(s)'.format(n, s, result))

    fptr.close()
