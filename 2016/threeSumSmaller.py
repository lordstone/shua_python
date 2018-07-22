class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        start, mid, end = len(nums) - 3, len(nums) - 2, len(nums) - 1
        while end >= 2:  # s, m, e = 0, 1, 2
            mid = end - 1
            while mid >= 1:
                v = target - nums[end] - nums[mid]
                start = max(min(mid - 1, start), 0)
                while start < mid - 1 and nums[start] < v:
                    start += 1
                while start >= 0 and nums[start] >= v:
                    start -= 1
                print(str(start) + ' ' + str(mid) + ' ' + str(end))
                res += start + 1
                mid -= 1
            end -= 1
        return res

sol = Solution()
inputList = [1,2,3,4,5,6,7,8,9,10]
inputList.sort()
inputTarget = 20
print(sol.threeSumSmaller(inputList, inputTarget))


