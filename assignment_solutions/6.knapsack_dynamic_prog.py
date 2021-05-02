# Uses python3
import sys
import numpy

def optimal_weight(W, wt):
        wt.insert(0, 0)
        matrix = numpy.zeros((len(wt), W + 1))
        for i in range(len(wt)):
            for w in range(W + 1):
                if w == 0 or i == 0:
                    matrix[i][w] = 0
                elif wt[i] <= w:
                    matrix[i][w] = max(wt[i] + matrix[i - 1][w - wt[i]], matrix[i - 1][w])
                else:
                    matrix[i][w] = matrix[i - 1][w]

        return int(matrix[i][w])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
