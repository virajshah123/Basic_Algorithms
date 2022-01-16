def get_change(m):
    counter = 0
    while(m > 0):
        if(m - 10 >= 0):
            m -= 10
            counter += 1
        elif(m - 5 >= 0): 
            m -= 5
            counter += 1
        elif(m - 1 >= 0):
            m -= 1
            counter += 1
    return counter

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
