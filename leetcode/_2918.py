import unittest
from typing import List

from parameterized import parameterized

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sum = sum(nums1)
        nums2_sum = sum(nums2)
        nums1_zeros = nums1.count(0)
        nums2_zeros = nums2.count(0)
        min_num1_sum = nums1_zeros + nums1_sum
        min_num2_sum = nums2_zeros + nums2_sum
        if nums1_zeros == 0 and nums2_zeros == 0 and min_num1_sum != min_num2_sum:
            return -1
        if nums1_zeros > 0 and nums2_zeros == 0 and min_num1_sum > min_num2_sum:
            return -1
        if nums2_zeros > 0 and nums1_zeros == 0 and min_num2_sum > min_num1_sum:
            return -1
        return max(min_num1_sum, min_num2_sum)


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[3,2,0,1,0], [6,5,0], 12],
        [[2,0,2,0], [1,4], -1],
        [[17,1,13,12,3,13], [2,25], -1],
    ])
    def test(self, n1, n2, exp):
        s = Solution()
        act_n = s.minSum(n1, n2)
        self.assertEqual(exp, act_n)

