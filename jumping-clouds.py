"""
This easy difficulty exercise was taken from
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
"""

def jumpingOnClouds(c):
    """
    Count jumps required to finish the game
    """
    jumps_required = 0
    current_step = 0
    is_not_finished = True
    while is_not_finished:
        try:
            current_step += 1 if c[current_step + 2] else 2
        except IndexError:
            is_not_finished = False
            if current_step == len(c) - 1:
                break
        jumps_required += 1        
    return jumps_required


if __name__ == '__main__':
    fptr = open('jumping-clouds-output.txt', 'w')

    n = int(input('Number of clouds (between 2 and 100): '))

    # Checking constrains
    while n < 2 or n > 100:
        print('\nThe number of clouds must be between 2 and 100')
        n = int(input('Number of clouds (between 2 and 100): '))

    c = list(map(int, input('Array of binary integers ({} integers): '.format(n)).rstrip().split()))

    # Checking constrains
    has_consecutive_ones = [True for i in range(len(c)-1) if c[i] == c[i+1] and c[i]]
    while not set(c).issubset({0, 1}) or len(c) != n or has_consecutive_ones or c[0] or c[len(c)-1]:
        print('\nIt must contain only 0 and 1\nFirst and last clouds must be 0\nThe array must have length {}\nThere cannot be two 1 consecutively'.format(n))
        c = list(map(int, input('Array of binary integers ({} integers): '.format(n)).rstrip().split()))
        has_consecutive_ones = [True for i in range(len(c)-1) if c[i] == c[i+1] and c[i]]

    result = jumpingOnClouds(c)

    fptr.write('Required jumps for n={} and c={}: {}'.format(n, c, result))

    fptr.close()
