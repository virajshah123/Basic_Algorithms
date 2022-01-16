
def optimal_summands(n):
    summands = [0]
    remaining = n

    while(remaining > 0):
        nextNum = summands[-1] + 1 

        if(remaining >= nextNum):
            remaining -= nextNum
            summands.append(nextNum)
        else:
            summands[-1] += remaining
            remaining = 0
    
    summands.pop(0)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
