
def lcs2(a, b):
    len_a = len(a)
    len_b = len(b)
    # initialize lcs
    lcs = []
    for i in range(len_a+1):
        row = [0]*(len_b+1)
        lcs.append(row)
    
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            up = lcs[i-1][j]
            left = lcs[i][j-1]
            diagonal = 0
            if(a[i-1] == b[j-1]):
                diagonal = lcs[i-1][j-1] + 1
            lcs[i][j] = max(up, left, diagonal)
    #print(lcs)
    return lcs[-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    
    print(lcs2(a, b))
