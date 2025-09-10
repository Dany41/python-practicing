import unittest
from typing import List

from parameterized import parameterized

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while i < (n / 2) + 1:
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]
            i += 1
        return []


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [2, [1,1]],
        [11, [2,9]],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.getNoZeroIntegers(nums1)
        self.assertEqual(exp_nums, act_n)