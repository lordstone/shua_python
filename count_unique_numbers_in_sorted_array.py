from typing import Any, List


def assert_or_print(actual_res: Any, exp_res: Any):
    if actual_res != exp_res:
        print(f"actual result: {actual_res}, expected result: {exp_res}")


def count_unique_numbers(nums: List[int]) -> int:
    """
    input arrays are sorted incrementally and with many duplicate numbers.
    """

    def divide_conquer(nums: List[int], a: int, b: int) -> List[int]:
        """
        Returns [num of unique, leftmost num, rightmost num]
        """
        if a == b:
            return [1, nums[a], nums[b]]
        mid = (a + b) // 2
        unique_a, a_left, a_right = divide_conquer(nums, a, mid)
        unique_b, b_left, b_right = divide_conquer(nums, mid + 1, b)
        a_b = unique_a + unique_b
        if b_left == a_right:
            a_b -= 1
        return [a_b, a_left, b_right]

    return divide_conquer(nums, 0, len(nums) - 1)[0]


def main():
    assert_or_print(count_unique_numbers([0]), 1)
    assert_or_print(count_unique_numbers([0, 0]), 1)
    assert_or_print(count_unique_numbers([0, 1]), 2)
    assert_or_print(count_unique_numbers([0, 0, 1]), 2)
    assert_or_print(count_unique_numbers([0, 0, 0]), 1)
    assert_or_print(count_unique_numbers([0, 0, 0, 0]), 1)
    assert_or_print(count_unique_numbers([0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3]), 4)


if __name__ == "__main__":
    main()
