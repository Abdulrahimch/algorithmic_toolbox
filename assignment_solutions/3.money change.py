# Uses python3
import sys

def get_change(m):

    if m >= 10:
        number_of_tens = m // 10
        m -= number_of_tens * 10

    if m >= 5:
        number_of_fives = m // 5
        m -= number_of_fives * 5

    if m >= 1:
        number_of_ones = m
        m -= number_of_ones

    number_of_coins = number_of_tens + number_of_fives + number_of_ones
    return number_of_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))