
def get_change(m):
    # handle base cases
    if m < 3:
        return m
    elif m == 3:
        return 1 
    
    # memoization
    money_list = [0]*(m+1)
    money_list[0], money_list[1], money_list[2], money_list[3] = 0, 1, 2, 1
    for i in range(4, m+1):
        minimum = min(money_list[i-1] + 1, money_list[i-3] + 1, money_list[i-4] + 1)
        money_list[i] = minimum
    
    #print(money_list)
    return money_list[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
