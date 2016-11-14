class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        best, bestS = 1, [0, 0]
        for i in range(len(s)):
            for j in range(i):
                dp[j][i] = (s[j] == s[i] and (i - j < 2 or dp[j+1][i-1]))
                if dp[j][i] and i - j + 1 > best:
                    best = i - j + 1
                    bestS = [i, j]
            dp[i][i] = 1
        [i, j] = bestS
        return s[j: i + 1]
