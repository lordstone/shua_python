import random


def generateRotatedArray(n=100, num_range=100):
    r = []
    random.seed()
    for i in range(0, n):
        r.append(random.randint(0, num_range))
    r.sort()
    c = random.randint(0, n)
    return r[c:] + r[:c]


a = generateRotatedArray()


print(str(a))


def findMinInRotatedArray(l):
    if l is None or len(l) == 0:
        raise ValueError('Empty Array Input')
    p1, p2, pm = 0, len(l)-1, 0
    while l[p1] >= l[p2]:
        if p2 - p1 == 1:
            pm = p2
            break
        pm = (p1 + p2) // 2
        if l[p1] == l[p2] == l[pm]:
            minNum = l[p1]
            for i in range(p1+1, p2+1):
                if minNum > l[i]:
                    minNum = l[i]
            return minNum
        if l[pm] >= l[p1]:
            p1 = pm
        elif l[pm] <= l[p2]:
            p2 = pm

    return l[pm]


print(findMinInRotatedArray(a))
