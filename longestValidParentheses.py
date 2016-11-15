class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        dp = [-1] * len(s)
        best, cur, stack = 0, 0, []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    t = stack.pop()
                    dp[t] = i
                    dp[i] = t
        for i in range(len(s)):
            if dp[i] != -1:
                cur += 1
            else:
                cur = 0
            best = max(cur, best)
        return best
