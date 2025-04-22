import math
import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        diff_n = len(differences)
        allowed_diff = upper - lower
        min_bound = 0
        max_bound = 0
        accumulator = 0
        i = 0
        while i < diff_n:
            accumulator = accumulator + differences[i]
            if accumulator > max_bound:
                max_bound = accumulator
            if accumulator < min_bound:
                min_bound = accumulator
            i += 1

        bound_len = (max_bound - min_bound)
        if allowed_diff >= bound_len:
            return allowed_diff - bound_len + 1
        else:
            return 0


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[1, -3, 4], 1, 6, 2],
        [[3,-4,5,1,-2], -4, 5, 4],
        [[4,-7,2], 3, 6, 0],
        [[-40], -46, 53, 60],
        [[83702,-5216], -82788, 14602, 13689],
        [[53121,38601,47753], -83297, 63538, 7361],
    ])
    def test(self, nums1, lower, upper, exp_nums):
        s = Solution()
        act_n = s.numberOfArrays(nums1, lower, upper)
        self.assertEqual(exp_nums, act_n)

