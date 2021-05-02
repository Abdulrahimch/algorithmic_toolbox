def max_pairwise_product(numbers):
    n = len(numbers)
    max_two_numbers = [0,0]
    for item in range(n):
       if numbers[item] > max_two_numbers[0]:
           max_two_numbers[0] = numbers[item]
           if max_two_numbers[0] > max_two_numbers[1]:
               max_two_numbers[1], max_two_numbers[0] = max_two_numbers[0], max_two_numbers[1]
    max_product = max_two_numbers[0] * max_two_numbers[1]
    return max_product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))