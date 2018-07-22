class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if d == 0: return 'NaN'
        if n == 0: return '0'
        sign_flag = (n < 0) ^ (d < 0)
        n = abs(n)
        d = abs(d)
        ans = str(n // d)
        if sign_flag:
            ans = '-' + ans
        if n % d == 0: return ans
        dic = {}
        n %= d
        ans += '.'
        while n not in dic:
            dic[n] = len(ans)
            n *= 10
            tmp = n // d
            ans += str(tmp)
            if n % d == 0: break
            n %= d
        if n in dic:
            ans = ans[:dic[n]] + '(' + ans[dic[n]:] + ')'

        return ans


s = Solution()

n, d = 2, 3
print(s.fractionToDecimal(n, d))

n, d = 4, 333
print(s.fractionToDecimal(n, d))

n, d = 561, 12736
print(s.fractionToDecimal(n, d))
