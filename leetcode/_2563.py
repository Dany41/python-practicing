import unittest
from typing import List

from parameterized import parameterized

def lower_bound(nums, low, high, value):
    while low <= high:
        mid = int(low + (high - low) / 2)
        if nums[mid] >= value:
            high = mid -1
        else:
            low = mid + 1
    return low


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        fair_count = 0
        sorted_nums = sorted(nums)
        i = 0
        while i < n - 1:
            min_allowed = lower - sorted_nums[i]
            max_allowed = upper + 1 - sorted_nums[i]
            min_bound = lower_bound(sorted_nums, i + 1, n - 1, min_allowed)
            max_bound = lower_bound(sorted_nums, i + 1, n - 1, max_allowed)
            fair_count += max_bound - min_bound
            i += 1

        return fair_count


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[0,1,7,4,4,5], 3, 6, 6],
        [[1,7,9,2,5], 11, 11, 1],
        [[-5,-7,-5,-7,-5], -12, -12, 6],
        [[0,0,0,0,0,0], 0, 0, 15],
        [[0,0,0,0,0,0], -1000000000, 1000000000, 15],
    ])
    def test(self, nums1, lower, upper, exp_nums):
        s = Solution()
        act_n = s.countFairPairs(nums1, lower, upper)
        self.assertEqual(exp_nums, act_n)

