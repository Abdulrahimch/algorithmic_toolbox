#Uses python3

import sys
import numpy


def lcs2(s1, s2, n1, n2):
    """ Finds the length of the longest common subsequence of two strings
    (str, str, int, int) -> (int, 2D-array) """

    # Initializing the matrix
    Matrix = numpy.zeros((n1 + 1, n2 + 1))
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                Matrix[i][j] = Matrix[i - 1][j - 1] + 1
            if s1[i - 1] != s2[j - 1]:
                Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])

    return (int(Matrix[n1][n2]), Matrix)
    #return int((Matrix[n1][n2]).max())
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

print(lcs2(a, b, n, m))



