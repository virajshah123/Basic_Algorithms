
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0

    if right - left <= 1:
        return number_of_inversions

    mid = int((left + right) / 2)
    #print(f'mid: {mid}')
    number_of_inversions += get_number_of_inversions(a, b, left, mid)
    number_of_inversions += get_number_of_inversions(a, b, mid, right)
    
    b1, b2 = [], []
    for i in range(left, mid):
        b1.append(b[i])
    for i in range(mid, right):
        b2.append(b[i])
    
    #print(f"{b1}, {b2}")
    
    indexCounter = left
    while(len(b1) > 0 and len(b2) > 0):
        #print("entered")

        if(b1[0] > b2[0]):
            number_of_inversions += len(b1)
            b[indexCounter] = b2[0]
            b2.pop(0)
            #print("updated")

        else:
            b[indexCounter] = b1[0]
            b1.pop(0)
            #print("updated")
        
        indexCounter += 1
        #print("exited")
    #print(f"before:{b}")
    
    for i in range(len(b1)):
        b[i+indexCounter] = b1[i]
    for i in range(len(b2)):
        b[i+indexCounter] = b2[i]
    #print(f"after:{b}")

    return number_of_inversions

if __name__ == '__main__':
    n = int(input())
    l2 = input()
    a = list(map(int, l2.split()))
    print(get_number_of_inversions(a, a, 0, len(a)))
    #print(get_number_of_inversions([3,1,2],[3, 1, 2], 0, 3))
