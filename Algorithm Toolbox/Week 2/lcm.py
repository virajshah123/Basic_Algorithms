# Uses python3
import sys

def lcm_naive(a, b):
    gcd = gcd_naive(a, b)
    return int(a*b/gcd)

def gcd_naive(a, b):
    if(a == 0 or b == 0):
        return max(a,b)

    maximum = max(a,b)
    minimum = min(a,b)

    return gcd_naive(maximum%minimum,minimum)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

