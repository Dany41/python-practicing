import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        c = 0
        while i < n:
            if nums[i] > nums[(i+1)%n]:
                c += 1
            i += 1
        return c <= 1


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[3,4,5,1,2], True],
        [[2,1,3,4], False],
        [[1,2,3], True],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.check(nums1)
        self.assertEqual(exp_nums, act_n)

