
def optimal_points(segments):
    points = []
    #write your code here
    while(len(segments) > 0):
        rightMin = segments[0][1]

        for i in range(len(segments)):
            if(segments[i][1] < rightMin):
                rightMin = segments[i][1]

        points.append(rightMin)

        flag = True
        index = 0
        while flag:
            if(index >= len(segments)):
                flag = False
                break
                
            #print(f"index: {index}, list length: {len(segments)}")

            if(segments[index][0] <= rightMin and rightMin <= segments[index][1]):
                segments.pop(index)
                index -= 1
            
            index += 1

    return points

if __name__ == '__main__':
    segments = []
    n = int(input())
    for i in range(n):
        x = input()
        segments.append(list(map(int, x.split())))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
