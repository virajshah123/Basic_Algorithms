
def optimal_sequence(n):
    # base case
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    elif n == 3:
        return [1, 3]

    # memoization
    sequence_list = [0]*(n+1) 
    sequence_list[0], sequence_list[1], sequence_list[2], sequence_list[3] = [], [1], [1, 2], [1, 3]

    # print(sequence_list)
    for i in range(4, n+1):   
        #print(sequence_list) 
        sequence1, sequence2, sequence3 = [], [], []
        if i % 2 == 0:
            sequence2 = sequence_list[int(i/2)][::]
            sequence2.append(i)
        if i % 3 == 0:
            sequence3 = sequence_list[int(i/3)][::]
            sequence3.append(i)
        sequence1 = sequence_list[i-1][::]
        sequence1.append(i)

        len1, len2, len3 = len(sequence1), len(sequence2), len(sequence3)
        # print(sequence1)
        # print(sequence2)
        # print(sequence3)
        if len2 == 0:
            len2 = float('inf')
        if len3 == 0:
            len3 = float('inf')
        # print(len1)
        # print(len2)
        # print(len3)
        if (len1 <= len2 and len1 <= len3):
            #print("in")
            sequence_list[i] = sequence1
        elif (len2 <= len1 and len2 <= len3):
            sequence_list[i] = sequence2
        elif(len3 <= len1 and len3 <= len2):
            sequence_list[i] = sequence3 
    
    return sequence_list[n]

if __name__ == '__main__':
    n = int(input())
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
