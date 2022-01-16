
def binary_search(keys, query):
    low, high = 0, len(keys) - 1

    while(low <= high):
        index = int((low + high) / 2)
        if(keys[index] == query):
            return index
        elif(keys[index] < query):
            low = index + 1
        else:
            high = index - 1

    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
