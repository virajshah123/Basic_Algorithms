# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(i, j):
    minimum = float('inf')
    maximum = 0-float('inf')
    for k in range(i,j):
        a = evalt(max_list[i][k],max_list[k+1][j],operations[k-1])
        b = evalt(max_list[i][k],min_list[k+1][j],operations[k-1])
        c = evalt(min_list[i][k],max_list[k+1][j],operations[k-1])
        d = evalt(min_list[i][k],min_list[k+1][j],operations[k-1])
        minimum = min(a,b,c,d,minimum)
        maximum = max(a,b,c,d,maximum)
    return minimum, maximum

def get_maximum_value():

    for s in range(1, n):
        for i in range(1, n-s+1):
            j = i+s
            min_list[i][j], max_list[i][j] = min_max(i,j)

    return max_list[1][n]


line = input()
digits = []
operations = []
for i in range(len(line)):
    if i%2 == 0:
        digits.append(int(line[i]))
    else:
        operations.append(line[i])

max_list = []
min_list = []
n = len(digits)
for i in range(n+1):
    max_list.append([0 for i in range(n+1)])
    min_list.append([0 for i in range(n+1)])
for i in range(n+1):
    max_list[i][i], min_list[i][i] = digits[i-1], digits[i-1]

print(get_maximum_value())




