import unittest
from typing import List

from parameterized import parameterized
from functools import cache



class Solution:

    visited = None

    def helper(self, nums: List[int], indexes: List[int]):
        if self.visited is None:
            self.visited = []
        self.visited.append(indexes)
        n = len(indexes)
        if n == 0: return 0
        res = nums[indexes[0]]
        i = 1
        while i < n:
            res ^= nums[indexes[i]]
            i += 1
        i = 0
        while i < n:
            new_indexes = indexes[:i] + indexes[(i + 1):]
            if new_indexes not in self.visited:
                res += self.helper(nums, new_indexes)
            i += 1
        return res

    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        indexes = [x for x in range(n)]
        return self.helper(nums, indexes)


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[], 0],
        [[1,3], 6],
        [[5,1,6], 28],
        [[3,4,5,6,7,8], 480],
        [[5,17,17,12,17], 464],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.subsetXORSum(nums1)
        self.assertEqual(exp_nums, act_n)

