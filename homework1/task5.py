"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""


def find_maximal_subarray_sum(nums, k) -> int:
    max_sum = float("inf")
    for subarray in range(1, k + 1):
        for starting_point in range(len(nums) - subarray + 1):
            new_sum = sum(nums[starting_point : starting_point + subarray])
            if new_sum > max_sum:
                new_sum = max_sum

    return new_sum
