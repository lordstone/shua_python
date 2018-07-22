class SolutionII(object):
    def singleNumberII(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            mask = 1 << i
            count = sum(1 for i in nums if i & mask)
            res |= mask if count % 3 == 1 else 0
        if res > 0x7fffffff:  # python does not have 32-bit limit for int,
            res -= 4294967296  # so have to show the negativity by subtracting all ones
        return res


class SolutionI(object):
    def singleNumberI(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res


class SolutionIII(object):
    def singleNumberIII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for n in nums:
            res ^= n
        diff = res & (- res)
        r1 = r2 = 0
        for n in nums:
            if n & diff:
                r1 ^= n
            else:
                r2 ^= n
        return [r1, r2]
