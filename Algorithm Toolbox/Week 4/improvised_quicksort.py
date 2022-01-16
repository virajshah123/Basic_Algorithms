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

def partition2(a, l, r):
    # original
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


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


if __name__ == '__main__':
    n = int(input())
    l2 = input()
    a = list(map(int, l2.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
