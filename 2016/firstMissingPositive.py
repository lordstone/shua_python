INT_MAX = 0x7fffffff


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def swap(a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp

        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[i] >= 1 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                n = nums[i]
                swap(n - 1, i)
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


s = Solution()
l = [1,2,3,5,0,-3]
s.firstMissingPositive(l)
