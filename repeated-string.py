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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
