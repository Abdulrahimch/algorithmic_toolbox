import sys

def lcm_fast_algo(a,b):
    if b > a:
        a, b = b, a

    lcm = a
    while lcm % b != 0:
        lcm += a
    return lcm

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    #print(lcm_naive(a, b))
    print(lcm_fast_algo(a, b))