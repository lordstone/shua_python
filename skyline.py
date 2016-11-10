import operator


def getSkyline(buildings):
    skylines = [[[i[0], i[2]], [i[1], 0]] for i in buildings]
    # skylines.sort(key=operator.itemgetter(0))
    if len(skylines) == 0:
        return []

    def merge_two(s1, s2):
        p1 = p2 = 0
        s = []
        bar1 = bar2 = -1
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1][0] == s2[p2][0]:

                higher = max(s1[p1][1], s2[p2][1])
                # if higher > bar1 and higher > bar2:

                if max(bar1, bar2) != higher:
                    s.append([s1[p1][0], higher])
                bar1 = max(bar1, s1[p1][1])
                bar2 = max(bar2, s2[p2][1])
                p1 += 1
                p2 += 1

            elif s1[p1][0] < s2[p2][0]:
                height = s1[p1][1]
                if height > bar2:
                    s.append([s1[p1][0], height])
                elif height < bar2:
                    if bar1 > bar2:
                        s.append([s1[p1][0], bar2])
                bar1 = height
                p1 += 1

            elif s2[p2][0] < s1[p1][0]:
                height = s2[p2][1]
                if height > bar1:
                    s.append([s2[p2][0], height])
                elif height < bar1:
                    if bar2 > bar1:
                        s.append([s2[p2][0], bar1])
                bar2 = height
                p2 += 1

        while p1 < len(s1):
            s.append([s1[p1][0], s1[p1][1]])
            p1 += 1
        while p2 < len(s2):
            s.append([s2[p2][0], s2[p2][1]])
            p2 += 1
        return s

    while len(skylines) > 1:
        sk = []
        for i in range(1, len(skylines), 2):
            sk.append(merge_two(skylines[i-1], skylines[i]))
        if len(skylines) % 2 == 1:
            sk.append(skylines[-1])
        skylines = sk[:]

    return skylines[0]


s = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
s1 = [[0,2,3],[2,5,3]]
s2 = [[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
s3 = [[4,10,10],[5,10,9],[6,10,8],[7,10,7],[8,10,6],[9,10,5]]
s4 = [[0,2,3],[2,5,3]]
ans = getSkyline(s4)
print(ans)
