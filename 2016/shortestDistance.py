class StupidSolution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        best = -1
        numBuildings = sum(x.count(1) for x in grid)

        buildings = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buildings.append((i, j))

        def calculateMetricCosts(x, y):
            return sum(abs(x - a) + abs(y - b) for a, b in buildings)

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                if best != -1 and calculateMetricCosts(i, j) >= best:
                    continue
                dq = collections.deque()
                cset = set((i, j))
                dq.append((i, j, 0))
                cost, buildingCovered = 0, 0
                while len(dq) > 0:
                    x, y, curCost = dq.popleft()

                    if grid[x][y] == 1:
                        cost += curCost
                        buildingCovered += 1
                    elif grid[x][y] == 0:
                        # start iterate over its neighboring cells
                        for a in [x - 1, x + 1]:
                            if a >= 0 and a <= n - 1 and (a, y) not in cset:
                                cset.add((a, y))
                                if grid[a][y] < 2:
                                    dq.append((a, y, curCost + 1))

                        for a in [y - 1, y + 1]:
                            if a >= 0 and a <= m - 1 and (x, a) not in cset:
                                cset.add((x, a))
                                if grid[x][a] < 2:
                                    dq.append((x, a, curCost + 1))
                    if buildingCovered == numBuildings:
                        if best == -1 or cost < best:
                            best = cost
                        break
                    if best != -1 and cost > best:
                        break

        return best