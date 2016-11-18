def countSort(a):
    k = [0] * (max(a) + 1)
    b = [0] * len(a)

    for e in a:
        k[e] += 1

    s = 0
    for i in xrange(len(k)):
        oldS = s
        s += k[i]
        k[i] = oldS

    for e in a:
        b[k[e]] = e
        k[e] += 1
    return b

# TODO
def howManyElements(arr, a, b):
    k = [0] * (max(arr) + 1)

    for e in arr:
        k[e] += 1

    print k
    s = 0
    for i in xrange(len(k)):
        oldS = s
        s += k[i]
        k[i] = oldS
    print k

    return k[b] - k[a]

r = [2, 5, 3, 0, 2, 3, 0, 3]
print countSort(r)
print howManyElements(r, 0, 0)