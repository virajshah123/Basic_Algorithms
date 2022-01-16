# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    pisanoPeriod = [0,1]
   
    while ((pisanoPeriod[-2] != 0 or pisanoPeriod[-1] != 1) or (len(pisanoPeriod) == 2)):
        nextNum = (pisanoPeriod[-1]+pisanoPeriod[-2]) % 10
        pisanoPeriod.append(nextNum)
    
    pisanoPeriod.pop()
    pisanoPeriod.pop()
    periodLen = len(pisanoPeriod)
    index_n = (n+2) % periodLen
    index_m = (m+1) % periodLen
    answer = (pisanoPeriod[index_n] - pisanoPeriod[index_m])%10
    return answer

if __name__ == '__main__':
    m, n = input().split()
    m, n = int(m), int(n)
    print(fibonacci_partial_sum_naive(m,n))
