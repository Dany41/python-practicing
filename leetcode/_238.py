import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cache = nums[0]
        zero_count = 1 if nums[0] == 0 else 0
        nums[0] = 1
        i = 1
        n = len(nums)
        while i < n:
            nums[0] *= nums[i]
            if nums[i] == 0:
                zero_count += 1
            i += 1

        if zero_count == 1:
            nums[0] = cache
            i = 0
            s = 1
            while i < n:
                if nums[i] != 0:
                    s *= nums[i]
                i += 1
            i = 0
            while i < n:
                if nums[i] == 0:
                    nums[i] = s
                else:
                    nums[i] = 0
                i += 1
            return nums
        elif zero_count > 1:
            return [0] * n
        else:
            i = 1
            while i < n:
                temp = nums[i]
                nums[i] = int((nums[i - 1] / temp) * cache if temp != 0 else nums[i - 1] * cache)
                cache = temp
                i += 1

        return nums


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[-1,1,0,-3,3], [0,0,9,0,0]],
        [[1,2,3,4], [24,12,8,6]],
        [[0,0], [0,0]],
        [[1,-1], [-1,1]],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.productExceptSelf(nums1)
        self.assertEqual(exp_nums, act_n)