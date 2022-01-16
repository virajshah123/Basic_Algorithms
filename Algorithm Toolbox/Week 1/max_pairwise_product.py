def max_pairwise_product(numbers):
    n = len(numbers)
    index_first = 0
    index_second = 0
    max_number = 0
    second_max_number = 0

    for index in range(n):
        if numbers[index] > max_number:
            max_number = numbers[index]
            index_first = index
        
    for index in range(n):
        if numbers[index] > second_max_number and index != index_first:
            second_max_number = numbers[index]
            index_second = index

    return max_number*second_max_number


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
