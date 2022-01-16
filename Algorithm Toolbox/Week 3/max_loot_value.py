
def get_optimal_value(capacity, weights, values):
    maxValue = 0

    while(capacity > 0 and sum(weights) != 0):
        maxUnitValue = float('-inf')
        indexOfMax = 0
        
       # print(weights,end = ' ')
       # print(values)
        for i in range(len(weights)):
            if (weights[i] > 0 and values[i]/weights[i] > maxUnitValue):
                maxUnitValue = values[i]/weights[i]
                indexOfMax = i
        #print(maxUnitValue)

        a = min(capacity, weights[indexOfMax])
        maxValue += a*maxUnitValue
        capacity -= a
        weights[indexOfMax] -= a   
        #print(f"Max Value: {maxValue}, capacity: {capacity}, weight of Max: {weights[indexOfMax]}")                   

    return maxValue


if __name__ == "__main__":
    x = input().split()
    n = int(x[0])
    capacity = int(x[1])
    weights = []
    values = []

    for i in range(n):
        t = input().split()
        value = int(t[0])
        weight = int(t[1])
        print(weight)
        weights.append(weight)
        values.append(value)

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
