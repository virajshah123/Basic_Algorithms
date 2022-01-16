
def is_majority(a, element):
    count = 0

    for i in a:
        if(element == i):
            count += 1

    if(count > int(n/2)):
        return True       
    else:
        return False

def get_majority_element(a, left, right):
    if left == right:
        return -1

    if left + 1 == right:
        return a[left]

    middle = int((left + right) / 2)
    maj1 = get_majority_element(a, left, middle)
    maj2 = get_majority_element(a,middle,right)

    if (maj1 == maj2):
        return maj1
    else:
        if is_majority(a, maj1):
            return maj1

        if is_majority(a, maj2):
            return maj2
    
    return -1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(get_majority_element(a, 0, n))
        print(1)
    else:
        print(0)
