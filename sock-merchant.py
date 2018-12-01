from math import floor
from itertools import groupby
    
# Sock merchant
def sockMerchant(n, ar):


    # Calculate sock pairs
    socks_pairs = 0
    sock_colors = set(ar)
    for color in sock_colors:
        socks_pairs += floor(ar.count(color) / 2)
        
    return socks_pairs



if __name__ == '__main__':
    fptr = open('sock-merchant-output.txt', 'w')

    n = int(input('Number of single socks: '))

    # Checking constrains
    while n < 1 or n > 100:
        print('You must select a number between 1 and 100')
        n = int(input('Number of single socks: '))
    
    ar = list(map(int, input('Socks colors ({} single socks): '.format(n)).rstrip().split()))
    
    # Checking constrains
    while (len(ar) is not n) or (max(ar) > 100) or (min(ar) < 1):
        print('The number of socks must be {} and colors must be between 1 and 100'.format(n))
        ar = list(map(int, input('Socks colors ({} single socks): '.format(n)).rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write('For n={} and ar={}, John can sell {} pairs'.format(n, ar, result))

    fptr.close()
