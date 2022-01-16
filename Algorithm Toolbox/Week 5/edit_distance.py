
def edit_distance(s, t):
    len_s = len(s)
    len_t = len(t)
    # initialize d
    d = []
    for i in range(len_s+1):
        if(i == 0):
            row = [x for x in range(len_t+1)]
        else:
            row = [0]*(len_t+1)
        d.append(row)
    for i in range(len_s+1):
        d[i][0] = i
    
    for i in range(1,len_s+1):
        for j in range(1,len_t+1):
            up = d[i-1][j] + 1
            left = d[i][j-1] + 1
            if(s[i-1] == t[j-1]):
                diagonal = d[i-1][j-1]
            else:
                diagonal = d[i-1][j-1] + 1
            d[i][j] = min(up, left, diagonal)
    return d[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
