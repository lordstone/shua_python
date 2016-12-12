class Solution(object):
    def __init__(self):
        self.mem = {}

    def solve(self, s):
        res = s
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i != 0 or s[:i] * (len(s) // i) != s: continue
            tmp = str(len(s) // i) + '[' + self.encode(s[:i]) + ']'
            if len(tmp) < len(res):
                res = tmp
        return res

    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1: return s
        if s in self.mem:
            return self.mem[s]
        best = s
        for i in range(1, len(s) + 1):
            first = s[:i]
            second = s[i:]
            res1 = self.solve(first)
            res2 = self.encode(second)
            if len(res1) + len(res2) < len(best):
                best = res1 + res2
        self.mem[s] = best
        return best