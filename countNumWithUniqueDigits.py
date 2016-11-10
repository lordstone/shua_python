# Given a non-negative integer n, count all numbers with unique digits


class Solution(object):

    @staticmethod
    def countNumbersWithUniqueDigits(n):
        """
        :type n: int
        :rtype: int
        """
        remainNum = 10
        dp = [1] + [0] * (n)
        for i in range(n):
            remainNum -= 1
            mysum = sum(dp)
            dp[i + 1] = dp[i] * remainNum + mysum
        return dp[n]
