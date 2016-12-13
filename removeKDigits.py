class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = ['0']
        for i in range(len(num)):
            while res[-1] > num[i] and len(res) + k > i + 1:
                res.pop()
            res.append(num[i])
        while len(res) > len(num) - k + 1:
            res.pop()
        return str(int(''.join(res)))


s = Solution()
s1 = '123129874198749187239287042981029380129831209401290912039128301298301294019'
print(s.removeKdigits(s1, 10))
