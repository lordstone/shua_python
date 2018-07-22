class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[j]: j += 1
        if j == len(s): return s
        return s[j:][::-1] + self.shortestPalindrome(s[:j]) + s[j:]
