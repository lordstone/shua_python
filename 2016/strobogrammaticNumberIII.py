SMAP = {1: 1, 0: 0, 8: 8, 6: 9, 9: 6}
SN = {0, 1, 6, 8, 9}
LM = {0: 4, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 2, 7: 2, 8: 1, 9: 0}
HM = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 4}


class FailedSolution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

        def isStro(w):
            for i in range(len(w) // 2):
                if w[i] != w[-1 * (i + 1)]:
                    return False
            return True

        if low == high:
            return 1 if isStro(low) else 0

        def genNum(length):
            num = 5 ** (length // 2)
            if length % 2 == 1:
                num *= 3
            return num

        res = 0

        def findSameLength(word1, word2):
            cur = genNum(len(word1))
            cur -= findAfter(word1)
            cur -= findPrev(word2)
            return cur

        def findPrev(word):
            if len(word) == 0:
                return 0
            res = 0
            for i in range(1, len(word) // 2):
                tmp = LM[int(word[i])]
                tmp *= genNum(len(word) - i * 2)
                res += tmp
            res += 1 if isStro(word) else 0
            return res

        def findAfter(word):
            if len(word) == 0:
                return 0
            res = 0
            for i in range(1, len(word) // 2):
                tmp = HM[int(word[i])]
                tmp *= genNum(len(word) - i * 2)
                res += tmp
            res += 1 if isStro(word) else 0
            return res

        if len(low) == len(high):
            res += findSameLength(low, high)
        else:
            res += findPrev(low)
            res += findAfter(high)
            for i in range(len(low) + 1, len(high)):
                res += genNum(i)
        return res


SN = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]
SAME = {'0', '1', '8'}


class Solution(object):

    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low) > int(high):
            return 0
        self.res = 0
        def DFS(n, word):
            if n == 0 and int(high) >= int(word) >= int(low):
                self.res += 1
                return
            if n % 2 == 1:
                for s in SAME:
                    DFS(n - 1, s)
            if n == 0 or n % 2 == 1:
                return
            start = int(n == 2)
            for i in range(start, 5):
                DFS(n-2, str(SN[i][0]) + word + str(SN[i][1]))

        for i in range(len(low), len(high)+1):
            DFS(i, "")
        return self.res


l, h = '100', '900'
s = Solution()
print(s.strobogrammaticInRange(l, h))
