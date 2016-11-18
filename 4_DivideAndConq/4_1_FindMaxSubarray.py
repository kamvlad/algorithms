def bruteForce(a):
    val = min(a)
    start = 0
    end = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            s = sum(a[i:j])
            if s >= val:
                start = i
                end = j - 1
                val = s
    return (val, start, end)

def linear(a):
    maxA = (a[0], 0, 0)
    curA = (a[0], 0, 0)

    for i in range(1, len(a)):
        if a[i] > 0 and curA[0] < 0:
            curA=(a[i], i, i)
        else:
            curA = (curA[0] + a[i], curA[1], curA[2] + 1)

        if curA[0] > maxA[0]:
            maxA = curA
    return maxA

#================
# Recursive
#================
def findRecursive(a, start, end):
    if start == end:
        return (a[start], start, end)

    midP = (start + end) >> 1
    left = findRecursive(a, start, midP)
    right = findRecursive(a, midP + 1, end)

    mLeft = (a[midP], midP)
    curSum = 0
    for i in range(midP, start - 1, -1):
        curSum += a[i]
        if curSum > mLeft[0]:
            mLeft = (curSum, i)

    mRight = (a[midP + 1], midP + 1)
    curSum = 0
    for i in range(midP + 1, end + 1):
        curSum += a[i]
        if curSum > mRight[0]:
            mRight = (curSum, i)
    mid = (mLeft[0] + mRight[0], mLeft[1], mRight[1])

    if mid[0] > left[0]:
        if mid[0] > right[0]:
            return mid
        else:
            return right
    else:
        if left[0] > right[0]:
            return left
        else:
            return right

def nlogn(a):
    return findRecursive(a, 0, len(a) - 1)

testA = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

def printRslt(a, r):
    print(r, a[r[1] : (r[2] + 1)])

printRslt(testA, bruteForce(testA))
printRslt(testA, nlogn(testA))
printRslt(testA, linear(testA))

