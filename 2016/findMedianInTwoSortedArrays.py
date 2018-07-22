def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    def findKth(arr1, arr2, k):
        if len(arr1) == 0:
            return arr2[k - 1]
        if len(arr2) == 0:
            return arr1[k - 1]
        if k == 1:
            return min(arr1[0], arr2[0])

        a = arr1[k // 2 - 1] if len(arr1) >= k // 2 else None
        b = arr2[k // 2 - 1] if len(arr2) >= k // 2 else None

        if b is None or (a is not None and a < b):
            return findKth(arr1[k // 2:], arr2, k - k // 2)
        return findKth(arr1, arr2[k // 2:], k - k // 2)

    n = len(nums1) + len(nums2)
    if n % 2 == 1:
        return findKth(nums1, nums2, n // 2 + 1)
    else:
        return (findKth(nums1, nums2, n // 2) + findKth(nums1, nums2, n // 2 + 1)) / 2.0


a, b = [1,2,3,4], [1,3,5,7,9]
a1, b1 = [1], [2, 3]
a2, b2 = [], [2, 3]
a3, b3 = [1, 2], [3, 4]
# print(findMedianSortedArrays(a1, b1))
# print(findMedianSortedArrays(a2, b2))
print(findMedianSortedArrays(a3, b3))
