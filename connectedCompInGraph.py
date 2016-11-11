def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    if n == 0:
        return 1 if len(edges) > 0 else 0
    arr = list(range(n))
    counter = n

    def connected(id1, id2):
        return getRoot(id1) == getRoot(id2)

    def getRoot(node):
        if arr[node] == node:
            return node
        arr[node] = getRoot(arr[node])
        return arr[node]

    def union(p, q):
        arr[getRoot(p)] = getRoot(q)

    for e in edges:
        a, b = e[0], e[1]
        if connected(a, b) is False:
            counter -= 1
        union(a, b)

    return counter


n1 = 5
p1 = [[0,1],[1,2],[2,3],[3,4]]
n2 = 4
p2 = [[0,1],[2,3],[1,2]]
n3 = 5
p3 = [[0,1],[0,2],[1,2],[2,3],[2,4]]
print(countComponents(n2, p2))
print(countComponents(n1, p1))
print(countComponents(n3, p3))
