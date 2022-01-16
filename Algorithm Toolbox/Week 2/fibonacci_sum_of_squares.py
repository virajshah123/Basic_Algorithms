# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    pisanoPeriod = [0,1]
   
    while ((pisanoPeriod[-2] != 0 or pisanoPeriod[-1] != 1) or (len(pisanoPeriod) == 2)):
        nextNum = (pisanoPeriod[-1]+pisanoPeriod[-2]) % 10
        pisanoPeriod.append(nextNum)
    
    pisanoPeriod.pop()
    pisanoPeriod.pop()
    periodLen = len(pisanoPeriod)
    index1 = n % periodLen
    index2 = (n+1) % periodLen

    return (pisanoPeriod[index1]*pisanoPeriod[index2])%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
