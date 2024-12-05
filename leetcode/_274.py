import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        paper_to_count = {}
        i = 0
        n = len(citations)
        citations_no_zeros = []
        while i < n:
            if citations[i] != 0:
                citations_no_zeros.append(citations[i])
            i += 1
        n = len(citations_no_zeros)
        if n <= 1:
            return n

        for key in citations:
            i = 1
            while i <= key:
                if i in paper_to_count:
                    paper_to_count[i] = paper_to_count[i] + 1
                else:
                    paper_to_count[i] = 1
                i += 1

        res = 0
        for key in paper_to_count.keys():
            if paper_to_count[key] >= key > res:
                res = key

        return res


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[3,0,6,1,5], 3],
        [[1,3,1], 1],
        [[100], 1],
        [[0], 0],
        [[11,15], 2],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.hIndex(nums1)
        self.assertEqual(exp_nums, act_n)

