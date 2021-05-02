import sys

def get_majority_element(a):
    dic = {}
    for i in a:
        dic[i] = 0

    for i in a:
        dic[i] += 1

    for i in dic.keys():
        if dic[i] > len(a) / 2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
