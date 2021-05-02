# Greatest common divisor
import sys

def gcd_naive(a,b):
    if b > a:
        a, b = b, a
    remaining = 1
    while remaining != 0:
        remaining = a % b
        a = b
        b = remaining
    return a

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))