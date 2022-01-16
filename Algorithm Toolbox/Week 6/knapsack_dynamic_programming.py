
def optimal_weight(W, w):
    # here the weights and the values are the same. 
    n = len(w)
    max_val = []
    for i in range(W+1):
        max_val.append([0 for i in range(n+1)])

    for i in range(1, W+1):
        for j in range(1, n+1):
            val1 = 0
            val2 = max_val[i][j-1]
            if i >= w[j-1]:
                val1 = max_val[i-w[j-1]][j-1] + w[j-1]
            max_val[i][j] = max(val1, val2)

    return max_val[W][n]

if __name__ == '__main__':
    W, n = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
