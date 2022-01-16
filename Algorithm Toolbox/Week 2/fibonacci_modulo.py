# Uses python3

def get_fibonacci_huge(n, m):
    pisanoPeriod = [0,1]
   
    while ((pisanoPeriod[-2] != 0 or pisanoPeriod[-1] != 1) or (len(pisanoPeriod) == 2)):
        nextNum = (pisanoPeriod[-1]+pisanoPeriod[-2]) % m
        pisanoPeriod.append(nextNum)
    
    pisanoPeriod.pop()
    pisanoPeriod.pop()
    periodLen = len(pisanoPeriod)
    index = n % periodLen

    return pisanoPeriod[index]

if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)
    print(get_fibonacci_huge(n, m))
