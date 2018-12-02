"""
This medium difficulty exercise was taken from
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

from math import ceil

def repeatedString(s, n):
    """
    Count a's occurencies in the first n characters
    """
    letter_to_count = 'a'
    s_len = len(s)
    s_rep = ceil(n / s_len)
    full_length = s_rep * s_len
    splitted_s = s[:full_length - n]
    complete_s_rep = s_rep - (1 if splitted_s else 0)
    return s.count(letter_to_count) * complete_s_rep + splitted_s.count(letter_to_count)


if __name__ == '__main__':
    fptr = open('repeated-string-output.txt', 'w')

    s = input('String to repeat (no more than 100 characters): ')

    # Checking constrains
    while len(s) < 1 or len(s) > 100:
        print('\nThe length of s must be between 1 and 100')
        s = input('String to repeat (no more than 100 characters): ')

    n = int(input('Number of characters to consider (no more than 10^12): '))

    # Checking constrains
    while n < 1 or n > 10**12:
        print('\nThe number of characters to consider cannot be more than 10^12')
        n = int(input('Number of characters to consider (no more than 10^12): '))

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
