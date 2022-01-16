# Uses python3
def calc_fib(n):
    if(n<=1):
        return n
    prev = 0
    current = 1
    for i in range(2,n+1):
        prev, current = current, prev+current
    return current

n = int(input())
print(calc_fib(n))
