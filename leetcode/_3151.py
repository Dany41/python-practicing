import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i] % 2 == 0 and nums[i+1] % 2 == 0 or nums[i] % 2 == 1 and nums[i+1] % 2 == 1:
                return False
            i += 1
        return True


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[1], True],
        [[2,1,4], True],
        [[4,3,1,6], False],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.isArraySpecial(nums1)
        self.assertEqual(exp_nums, act_n)

