import random

def partition3(a, l, r):
    # improvised to increase speed for equal entries.
    m1, m2 = l, l
    x = a[l]
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            m2 += 1
            a[i], a[m2] = a[m2], a[i]

        elif a[i] == x:
            m2 += 1 
            a[i], a[m2] = a[m2], a[i]
            a[m2], a[l + m2 - m1] = a[l + m2 - m1], a[m2]
        # print(f"array before: {a}")
        # print(f"indices: {m1}, {m2}")
    # print()

    if(m1 > l + m2 - m1):
        for i in range(l, l + m2 - m1 + 1):
            a[i], a[i + m1 - l] = a[i + m1 - l], a[i]
            # print(f"array after: {a}")
    else:
        for i in range(l, m1):
            a[i], a[i + m2 - m1 + 1] = a[i + m2 - m1 + 1], a[i]
            # print(f"array after: {a}")

    return m1, m2

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    
    m1, m2 = partition3(a, l, r)
    #print(a)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)

def fast_count_segments(starts, ends, points):
    count = {}
    for i in range(len(points)):
        count[points[i]] = 0

    a = {}
    for element in points:
        a[element] = 'point'
    for element in starts:
        a[element] = 'start'
    for element in ends:
        a[element] = 'end'
    b = list(a.keys())

    randomized_quick_sort(b, 0, len(b) - 1)
    print(b)

    numSegments = 0
    for element in b:
        if(a[element] == 'start'):
            numSegments += 1
        elif(a[element] == 'end'):
            numSegments -= 1
        elif(a[element] == 'point'):
            count[element] = numSegments     

    return list(count.values())

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    # l1 = input()
    # data = list(map(int, l1.split()))
    # s = data[0]
    # n = data[1]
    # starts, ends = [], []
    # for i in range(s):
    #     li = input().split()
    #     starts.append(int(li[0]))
    #     ends.append(int(li[1]))
    # l4 = input()
    # points = list(map(int, l4.split()))

    # cnt = fast_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')

    # for index in range(10):
    #     start, end, point = [], [], []
    #     for i in range(15):
    #         start.append(random.randint(1, 50))
    #         end.append(random.randint(1, 50))
    #     for i in range(10):
    #         point.append(random.randint(1, 50))

    #     cnt1 = fast_count_segments(start, end, point)
    #     cnt2 = naive_count_segments(start, end, point)
    #     for i in range(len(cnt1)):
    #         if(cnt1[i] != cnt2[i]):
    #             for x in start:
    #                 print(x, end=' ')
    #             print()
    #             for x in end:
    #                 print(x, end=' ')
    #             print()
    #             for x in point:
    #                 print(x, end=' ')
    #             print()
    #             print(f'Right: {cnt2}')
    #             print(f'Wrong: {cnt1}')  
    #             break 

    print("Right")
    start = [4, 5, 2, 3, 45, 23, 1]
    end = [7, 32, 3, 4, 53, 26, 9]
    point = [6, 7, 2, 1, 25, 55, 48, 4, 26, 3]
    cnt1 = naive_count_segments(start, end, point)
    for x in cnt1:
        print(x, end=' ')
    
    print()
    print("Wrong")
    cnt2 = fast_count_segments(start, end, point)
    for x in cnt2:
        print(x, end=' ')
