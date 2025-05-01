import unittest
from typing import List

from parameterized import parameterized

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        i = 0
        n = len(nums)
        while i < n:
            if len(str(nums[i])) % 2 == 0:
                res += 1
            i += 1
        return res


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[12,345,2,6,7896], 2],
        [[555,901,482,1771], 1],
    ])
    def test(self, n, exp):
        s = Solution()
        act_n = s.findNumbers(n)
        self.assertEqual(exp, act_n)

