def calc_fib(n):
    if n < 0:
        ValueError("Input 0 or greater only!")

    fibs = [0, 1]

    if n <= len(fibs) -1:
        return fibs[n]

    while n > len(fibs) -1:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

n = int(input())
print(calc_fib(n))