
def compute_min_refills(distance, tank, stops):
    new_stops = stops
    new_stops.append(distance)
    new_stops.insert(0, 0)
    minRefills = 0
    currentStop = 0
    lastRefill = 0
    while(currentStop < len(new_stops)):
        while(currentStop < len(new_stops) and new_stops[currentStop]-new_stops[lastRefill] <= tank):
            currentStop += 1
        if (currentStop-1 == lastRefill):
            return -1
        lastRefill = currentStop - 1 
        if(lastRefill < len(new_stops)-1):
            minRefills += 1
    return minRefills

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    input()
    stops = list(map(int,input().split()))
    print(compute_min_refills(d, m, stops))
