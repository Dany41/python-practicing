import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        i = 0
        c = 0
        n = len(nums)
        d_s = {}
        while i < n:
            if (i - nums[i]) in d_s:
                d_s[i - nums[i]] += 1
            else:
                d_s[i - nums[i]] = 1
            i += 1

        i = 0
        while i < n:
            c += d_s[i - nums[i]] - 1
            d_s[i - nums[i]] -= 1
            i += 1

        return ((n * (n - 1)) / 2) - c


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[1,2,3,4,5], 0],
        [[4,1,3,3], 5],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.countBadPairs(nums1)
        self.assertEqual(exp_nums, act_n)

