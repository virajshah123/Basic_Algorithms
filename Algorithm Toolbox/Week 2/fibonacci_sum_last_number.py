# Uses python3
import sys

def fibonacci_sum_naive(n):
    pisanoPeriod = [0,1]
   
    while ((pisanoPeriod[-2] != 0 or pisanoPeriod[-1] != 1) or (len(pisanoPeriod) == 2)):
        nextNum = (pisanoPeriod[-1]+pisanoPeriod[-2]) % 10
        pisanoPeriod.append(nextNum)
    
    pisanoPeriod.pop()
    pisanoPeriod.pop()
    periodLen = len(pisanoPeriod)
    index = (n+2) % periodLen

    answer = pisanoPeriod[index]
    if(answer==0):
        return 9
    else:
        return answer-1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
