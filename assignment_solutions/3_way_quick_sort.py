import sys
import random

def partition3(a, l, r):
    less_than_poiniter = l  # the part that is less than pivot
    i = l  # We scan the array from left to right
    greater_than_pointer = r  # The part that is greater than the pivot
    pivot = a[l]  # The pivot, chosen to be the first element of the array
    # in the quick_sort function.
    while i <= greater_than_pointer:  # Starting from the first element.
        if a[i] < pivot:
            a[less_than_poiniter], a[i] = a[i], a[less_than_poiniter]
            less_than_poiniter += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[greater_than_pointer] = a[greater_than_pointer], a[i]
            greater_than_pointer -= 1
        else:
            i += 1

    return less_than_poiniter, greater_than_pointer

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);
    less_than_poiniter, greater_than_pointer = partition3(a, l, r)
    randomized_quick_sort(a, l, less_than_poiniter-1)
    randomized_quick_sort(a, greater_than_pointer+1, r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')