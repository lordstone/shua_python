import collections


# failed solution
def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    """
    if len(words) == 0:
        return ''
    paths, indegree, possibleStarts = collections.defaultdict(set), dict(), set()
    for w in words:
        for c in w:
            indegree[c] = 0
    for idx in range(len(words) - 1):
        if words[idx].startswith(words[idx + 1]) and len(words[idx]) > len(words[idx + 1]):
            return ''
        for i in range(len(words[idx])):
            if i >= len(words[idx + 1]):
                break
            a, b = words[idx][i], words[idx + 1][i]
            if a != b:
                possibleStarts.add(a)
                if a in paths:
                    if b not in paths[a]:
                        paths[a].add(b)
                        indegree[b] += 1
                else:
                    paths[a].add(b)
                    indegree[b] += 1
                break
    dq = collections.deque()
    for k in indegree:
        if indegree[k] == 0:
            dq.append(k)
    res = ''
    while len(dq) > 0:
        c = dq.popleft()
        res += c
        if c in paths:
            for nc in paths[c]:
                indegree[nc] -= 1
                if indegree[nc] == 0:
                    dq.append(nc)
    return res if len(indegree) == len(res) else ''


def alienOrderBetter(words):
    """
    :type words: List[str]
    :rtype: str
    """
    neigh = collections.defaultdict(set)
    pre = collections.defaultdict(set)
    for pair in zip(words, words[1:]):
        w1, w2 = pair
        if w1.startswith(w2) and len(w1) > len(w2):  # sanity check
            return ''
        for c1, c2 in zip(*pair):
            if c1 != c2:
                neigh[c1].add(c2)
                pre[c2].add(c1)
                break

    chars = set(''.join(words))
    stack = [c for c in chars if not pre[c]]  # these are heads
    res = ''
    # DFS
    while stack:
        ch = stack.pop()
        res += ch
        for nbr in neigh[ch]:
            pre[nbr].remove(ch)
            if not pre[nbr]:
                stack.append(nbr)
        pre.pop(ch)
    return res if not pre else ''


w1 = ['aab', 'acb', 'acd', 'ad', 'b', 'd', 'e']
w2 = ["wrtkj", "wrt"]
w3 = ["zy", "zx"]
print(alienOrder(w1))
print(alienOrder(w2))
print(alienOrder(w3))




