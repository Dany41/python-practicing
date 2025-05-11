import unittest
from typing import List

from parameterized import parameterized

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        counter = 0
        while i < n:
            if arr[i] % 2 == 1:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                return True
            i += 1
        return False


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[2,6,4,1], False],
        [[1,2,34,3,4,5,7,23,12], True],
    ])
    def test(self, n1, exp):
        s = Solution()
        act_n = s.threeConsecutiveOdds(n1)
        self.assertEqual(exp, act_n)

