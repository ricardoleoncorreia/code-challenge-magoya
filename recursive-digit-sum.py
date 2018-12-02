"""
This medium difficulty exercise was taken from
https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
"""

def superDigit(n, k):
    """
    Returns the superdigit of the number
    n repeated k times
    """
    nk = n * k
    n = str(sum([int(c) for c in nk]))
    return n if len(n) == 1 else superDigit(n, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
