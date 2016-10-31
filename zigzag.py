

def zigzag(l):
    l.sort()
    start, end = 0, len(l) - 1
    res = []
    moveLeft = True
    while start < end:
        if moveLeft is True:
            res.append(l[start])
            start += 1
        else:
            res.append(l[end])
            end -= 1
        moveLeft = not moveLeft
    return res


l = [2,3,5,2,3,6,8,3,5,7,10,24,123,25,92,4,2,3,5]
print(zigzag(l))


