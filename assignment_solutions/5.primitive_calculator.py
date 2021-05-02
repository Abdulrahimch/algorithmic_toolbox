import sys
import math

def optimal_sequence(n):
    no_of_operartions = {1: 0, 2: 1, 3: 1}
    min_operations = math.inf
    for i in range(4, n+1):
        if i % 3 == 0:
            result = i // 3
            if no_of_operartions[result] + 1 < min_operations:
                min_operations = no_of_operartions[result] + 1

        if i % 2 == 0:
            result = i // 2
            if no_of_operartions[result] + 1 < min_operations:
                min_operations = no_of_operartions[result] + 1

        if no_of_operartions[i-1] + 1 < min_operations:
            min_operations = no_of_operartions[i-1] + 1

        no_of_operartions[i] = min_operations
        min_operations = math.inf
    return no_of_operartions[n]

input = sys.stdin.read()
n = int(input)
print(optimal_sequence(n))
