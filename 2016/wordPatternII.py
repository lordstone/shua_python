class Solution(object):
    def wordPatternMatch(self, pattern, ins):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def dfs(s, p, h1, h2):  # h1: p: s, h2: s: p
            if len(p) == 0 and len(s) == 0: return True
            if len(p) == 0 or len(s) == 0: return False
            if p[0] not in h1:
                # take len from 0 to len(s) - len(p) for this p
                if len(p) == 1 and s not in h2: return True
                for i in range(1, len(s) - len(p) + 2):
                    if s[:i] in h2: continue
                    h1[p[0]] = s[:i]
                    h2[s[:i]] = p[0]
                    res = dfs(s[i:], p[1:], h1, h2)
                    if res: return True
                    del h1[p[0]]
                    del h2[s[:i]]
                return False
            else:
                next_s = h1[p[0]]
                if len(next_s) > len(s) or next_s != s[:len(next_s)]:
                    return False
                else:
                    return dfs(s[len(next_s):], p[1:], h1, h2)

        return dfs(ins, pattern, dict(), dict())


