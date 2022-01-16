import itertools

def partition3(A, n, x, y, z, collection):
    # # initialize the answer matrix.
    # is_possible_result = []
    # for i in range(pricePerPerson+1):
    #     is_possible_result.append([])
    #     for j in range(pricePerPerson+1):
    #         is_possible_result[i].append([])
    #         for k in range(pricePerPerson+1):
    #             is_possible_result[i][j].append(0)
    
    # for i in range(1, pricePerPerson+1):
    #     is_possible_result.append([])
    #     for j in range(1, pricePerPerson+1):
    #         is_possible_result[i].append([])
    #         for k in range(1, pricePerPerson+1):
    #             is_possible_result[i][j].append(0)

    # base cases
    if x==0 and y==0 and z==0:
        return 1
    if n<0:
        return 0
    
    val = (n,x,y,z)
    if val not in collection:
        part1, part2, part3 = 0,0,0
        if x >= A[n]:
            part1 = partition3(A, n-1, x-A[n],y,z,collection)
        if y >= A[n]:
            part2 = partition3(A, n-1, x,y-A[n],z,collection)
        if z >= A[n]:
            part3 = partition3(A, n-1, x,y,z-A[n],collection)
        
        if max(part1,part2,part3) == 1:
            collection[val] = 1
        else:
            collection[val] = 0
    return collection[val]
    

    return is_possible_result

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    collection = {}
    totalPrice = sum(A)
    if totalPrice % 3 != 0:
        print('0')
    elif n < 2:
        print("0") 
    else:
        pricePerPerson = int(totalPrice / 3)
        print(partition3(A, n-1, pricePerPerson, pricePerPerson, pricePerPerson, collection))


