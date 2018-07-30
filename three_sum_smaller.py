# lintcode 918 leetcode 259 locked
import unittest


class ThreeSumSmaller(object):
    def find_number(self, nums, target):
        if len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            cur = target - nums[i]
            while left < right:
                if nums[left] + nums[right] < cur:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res


class Test(unittest.TestCase):
    def test_findnumber(self):
        target = ThreeSumSmaller()
        l1 = [-2, 0, 1, 3]
        self.assertEqual(target.find_number(l1, 2), 2)

