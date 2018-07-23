# leetcode 215
import unittest


class Partitioner(object):
    @staticmethod
    def partition(nums, k, start=0, end=None):
        left = start + 1
        right = len(nums) - 1 if end is None else end
        if start == right:
            return start
        nums[start], nums[k] = nums[k], nums[start]
        while left < right:
            if nums[left] < nums[start]:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        if nums[start] > nums[left]:
            left -= 1
        nums[start], nums[left] = nums[left], nums[start]
        return left


class FindKthLargest(object):
    @staticmethod
    def find_kth(nums, k):
        # k starting from 1
        start, end = 0, len(nums) - 1
        pivot = Partitioner.partition(nums, start, start, end)
        while pivot != k - 1:
            if pivot > k - 1:
                end = pivot - 1
            else:
                start = pivot + 1
            pivot = Partitioner.partition(nums, start, start, end)
        return nums[pivot]


class Test(unittest.TestCase):
    def test_partition(self):
        nums1 = [3, 2, 7, 5, 9, 0, 1]
        pivot = Partitioner.partition(nums1, 3)
        self.assertEqual(pivot, 2, 'the pivot number is put wrong')
        self.assertEqual(nums1, [7, 9, 5, 3, 0, 1, 2], 'the pivot number is put wrong')

    def test_find_kth(self):
        nums1 = [3, 2, 6, 9, 0, 14, 1, 8]
        nums2 = [3, 2, 7, 5, 9, 0, 1]
        k1 = 4  # starting from 1
        k2 = 3
        self.assertEqual(FindKthLargest.find_kth(nums2, k2), 5)
        self.assertEqual(FindKthLargest.find_kth(nums1, k1), 6)
        self.assertEqual(FindKthLargest.find_kth([1, 1, 1], 1), 1)
        self.assertEqual(FindKthLargest.find_kth([1, 2, 0], 3), 0)
