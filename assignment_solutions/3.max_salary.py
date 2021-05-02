import sys


def is_greater_or_equal(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))

def largest_number(a):
    res = ''
    while a:
        max_digit = str(0)
        for digit in a:
            if is_greater_or_equal(digit, max_digit):
                max_digit = digit
        res += max_digit
        a.remove(max_digit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))