
def max_dot_product(a, b):
    dot_prod = 0

    while(len(a) > 0):
        max_a, max_b = a[0], b[0]
        index_a, index_b = 0, 0

        for i in range(len(a)):
            a_val, b_val = a[i], b[i]

            if(max_a < a_val):
                max_a = a_val
                index_a = i

            if(max_b < b_val):
                max_b = b_val
                index_b = i

        dot_prod += max_a*max_b
        a.pop(index_a)
        b.pop(index_b)

    return dot_prod    

if __name__ == '__main__':
    n = input()
    a = list(map(int, (input().split())))
    b = list(map(int, (input().split())))
    print(max_dot_product(a, b))
    
