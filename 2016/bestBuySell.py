class SolutionII(object):
    def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        curLow, curHigh, res = prices[0], prices[0], 0
        for i in range(1, len(prices)):
            p = prices[i]
            if p > curHigh:
                curHigh = p
            elif p < curHigh:
                if curHigh > curLow:
                    res += curHigh - curLow
                curHigh = p
                curLow = p
        if curHigh > curLow:
            res += curHigh - curLow
        return res


l = [6,1,3,2,4,7]
print(SolutionII.maxProfit(l))
