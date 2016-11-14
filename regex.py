class DPSolution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]


class TLESolution(object):
    # Not working w leetcode python: timeout
    @staticmethod
    def match(s, pattern):
        if s is None or pattern is None:
            return False
        if s == "" and pattern == "":
            return True
        elif s == "" and pattern != "":
            return False
        if s != "" and pattern == "":
            return False

        if len(pattern) > 1 and pattern[1] == '*':
            if pattern[0] == s[0] or (pattern[0] == '.' and len(s) > 0):
                return TLESolution.match(s[1:], pattern[2:]) \
                       or TLESolution.match(s[1:], pattern) \
                       or TLESolution.match(s, pattern[2:])
            else:
                return TLESolution.match(s, pattern[2:])

        if s[0] == pattern[0] or (pattern[0] == '.' and len(s) > 0):
            return TLESolution.match(s[1:], pattern[1:])

        return False

print(TLESolution.match("aaa", "aaaa"))

