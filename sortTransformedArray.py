def sortTransformedArray(nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """

    def f(x):
        return a * x ** 2 + b * x + c

    if a == 0:
        res = list(map(f, nums))
        if b < 0:
            res.reverse()
        return res

    extrema = -1 * (b) / (2 * a)
    cutoff = 0
    for cutoff in range(len(nums)):
        if nums[cutoff] > extrema:
            break
    res = []
    left, right = cutoff - 1, cutoff

    cmp = lambda x, y: x <= y
    if a < 0:
        cmp = lambda x, y: x >= y

    while left >= 0 and right < len(nums):
        lv, rv = f(nums[left]), f(nums[right])
        if cmp(rv, lv):
            res.append(rv)
            right += 1
        if cmp(lv, rv):
            res.append(lv)
            left -= 1
    while left >= 0:
        res.append(f(nums[left]))
        left -= 1
    while right < len(nums):
        res.append(f(nums[right]))
        right += 1
    if a < 0:
        res.reverse()
    return res


nums = [-9,-7,-3,-1, 0,1, 4, 8, 13]
a, b, c = -2, 0, 9
print(sortTransformedArray(nums, a, b, c))
