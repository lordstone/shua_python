class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        def idx(x):
            return (nums[x] + x) % len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            cur = i
            cando = True
            counter = 0
            nextCur = idx(cur)
            sign = 1 if nums[cur] > 0 else -1
            while nums[nextCur] != 0:
                cur = nextCur
                nextCur = idx(cur)
                if nums[cur] * sign < 0 or cur == nextCur:
                    cando = False
                    break
                nums[cur] = 0
                counter += 1
            if (not cando) or counter < 1:
                continue
            return True
        return False
