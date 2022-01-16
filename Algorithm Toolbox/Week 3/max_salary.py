
def isMaxDigits(a, b):
    aString, bString = str(a), str(b)
    num1 = int(aString + bString)
    num2 = int(bString + aString)

    if max(num1, num2) == num1:
        return True
    else:
        return False

def largest_number(a):
    largestNumber = ""
    while(len(a) > 0):
        maxDigit = a[0]
        maxIndex = 0

        for i in range(len(a)):
            if isMaxDigits(a[i],maxDigit):
                maxDigit = a[i]
                maxIndex = i

        largestNumber += str(maxDigit)
        a.pop(maxIndex)

    return largestNumber

if __name__ == '__main__':
    _ = input()
    data = list(map(int, input().split()))
    print(largest_number(data))
    
