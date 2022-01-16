import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def find_dist(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"

def minimum_distance(points):
    #print(points, end=' ')
    minDist = float('inf')
    points.sort(key = lambda point: point.x)
    #print(points, end='     ')

    # base step
    if(len(points) == 2):
        return points[0].find_dist(points[1])
    if(len(points) <= 1):
        return float('inf')   

    # recursive step
    mid = int(len(points) / 2)
    # print(points)
    # print(points[0 : mid])
    d1 = minimum_distance(points[0 : mid])
    d2 = minimum_distance(points[mid : len(points)])
    minDist = min(d1, d2)

    # calculate the points in the vertical strip
    mid_x = (points[mid-1].x + points[mid].x) / 2
    strip = []
    index = 0
    while(mid-index >= 0 and mid_x - points[mid-index].x <= minDist):
        strip.append(points[mid-index])
        index += 1
    index = 1
    while(mid+index < len(points) and points[mid+index].x - mid_x <= minDist):
        strip.append(points[mid+index])
        index += 1
    
    # sort it according to the y-coordinates
    strip.sort(key = lambda point: point.y)

    # calculate the minimum distance in this strip
    minDisStrip = float('inf')
    #print(strip)
    for i in range(len(strip)):
        index = i + 1
        while(index < len(strip) and strip[i].find_dist(strip[index]) < minDist):
            #print(f"Points {strip[i]} and {strip[index]} have dist {strip[i].find_dist(strip[index])}")
            minDisStrip = min(minDisStrip, strip[i].find_dist(strip[index]))
            index += 1
    #print(minDisStrip)

    return min(minDist, minDisStrip)

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        li = list(map(int, input().split()))
        points.append(Point(li[0],li[1]))

    print("{0:.4f}".format(minimum_distance(points)))
