class SlowSolution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0: return num
        if len(num) < 2: return '0'
        res, flag, zflag = '', False, False
        for i in range(len(num)):
            if flag or (i < len(num)-1 and num[i] <= num[i+1]):
                if num[i] != '0' or zflag:
                    res += num[i]
                    zflag = True
            else:
                flag = True
        if res == '': res = '0'
        return self.removeKdigits(res, k-1)
