# Uses python333

def get_fibonacci_last_digit_naive(n):
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10

    return current

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
