import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if len(A) == 0: return 0
        d1, d2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                d1[A[i] + B[j]] += 1
                d2[C[i] + D[j]] += 1
        res = 0
        for i in d1:
            if -i in d2:
                res += d1[i] * d2[-i]
        return res
