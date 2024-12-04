import unittest
from typing import List

from parameterized import parameterized

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        indexes = self.getIndexArrays(prices)
        i = 0
        n = len(indexes)
        res = 0
        if n == 1:
            return prices[len(prices) - 1] - prices[0]
        while i < n - 1:
            if indexes[i+1] - indexes[i] == 1:
                i += 1
                continue
            right_index = indexes[i + 1] - 1
            left_index = indexes[i]
            res += prices[right_index] - prices[left_index]
            i += 1
        res += prices[len(prices) - 1] - prices[indexes[len(indexes) - 1]]
        return res


    def getIndexArrays(self, prices: List[int]) -> List[int]:
        n = len(prices)
        indexes = [0]
        i = 0
        while i < n - 1:
            if prices[i] > prices[i + 1]:
                indexes.append(i + 1)
            i += 1
        return indexes


#if __name__ == "__main__":
#    unittest.main()

class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[7,1,5,3,6,4], [0,1,3,5]],
        [[1,2,3,4,5], [0]],
        [[7,6,4,3,1], [0,1,2,3,4]],
        [[7,2,3,4,1,5,3,9],[0,1,4,6]],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.getIndexArrays(nums1)
        self.assertEqual(exp_nums, act_n)
    @parameterized.expand([
        [[7,1,5,3,6,4], 7],
        [[1,2,3,4,5], 4],
        [[7,6,4,3,1], 0],
        [[7,2,3,4,1,5,3,9], 12],
    ])
    def testMaxProfit(self, nums1, exp_nums):
        s = Solution()
        act_n = s.maxProfit(nums1)
        self.assertEqual(exp_nums, act_n)