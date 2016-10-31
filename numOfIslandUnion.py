directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class StupidSolution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if m == 0 or n == 0 or len(positions) == 0:
            return res
        uf = [-1] * (m * n)
        count = 0

        for x, y in positions:
            idx = x * n + y
            if uf[idx] != -1:
                res.append(count)
            else:
                uf[idx] = idx
                count += 1

                for dx, dy in directions:
                    cx = x + dx
                    cy = y + dy
                    neighborIdx = cx * n + cy

                    if cx < 0 or cx >= m or cy < 0 or cy >= n:
                        continue

                    if uf[neighborIdx] == -1:
                        continue

                    def connected(id1, id2):
                        return uf[id1] == uf[id2]

                    def union(p, q):
                        p, q = uf[p], uf[q]
                        for idx, v in enumerate(uf):
                            if v == p:
                                uf[idx] = q

                    if connected(idx, neighborIdx) is False:
                        union(neighborIdx, idx)
                        count -= 1

                res.append(count)

        return res


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if m == 0 or n == 0 or len(positions) == 0:
            return res
        uf = list(range(m * n))
        sz = [0] * (m * n)
        count = 0

        for x, y in positions:
            idx = x * n + y
            sz[idx] += 1
            count += 1

            for dx, dy in directions:
                cx = x + dx
                cy = y + dy
                neighborIdx = cx * n + cy

                if cx < 0 or cx >= m or cy < 0 or cy >= n:
                    continue

                def getRoot(p):
                    while p != uf[p]:
                        uf[p] = uf[uf[p]]
                        p = uf[p]
                    return p

                def connected(id1, id2):
                    return getRoot(id1) == getRoot(id2)

                def union(p, q):
                    rp, rq = getRoot(p), getRoot(q)
                    if rp == rq:
                        return
                    if sz[p] < sz[q]:
                        uf[rp] = rq
                        sz[q] += sz[p]
                    else:
                        uf[rq] = rp
                        sz[p] += sz[q]

                if sz[neighborIdx] > 0:  # was placed island
                    if connected(idx, neighborIdx) is False:
                        union(neighborIdx, idx)
                        count -= 1

            res.append(count)
        return res