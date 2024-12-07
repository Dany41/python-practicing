import unittest
from typing import List

from parameterized import parameterized


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = []
        i = 0
        n = len(gas)
        sum_diff = 0

        while i < n:
            diffs.append(gas[i] - cost[i])
            sum_diff += diffs[i]
            i += 1

        if sum_diff >= 0:
            diffs_zipped = list(zip(diffs, range(0, n)))
            diffs_zipped = sorted(diffs_zipped, key=lambda x: x[0], reverse=True)
            for diff, i in diffs_zipped:
                if diff > 0:
                    j = 0
                    accum = 0
                    go_on = True
                    while j < n and go_on:
                        accum += diffs[(i + j) % n]
                        if accum < 0:
                            go_on = False
                        j += 1
                    if go_on:
                        return i
                i += 1
            return 0
        else:
            return -1


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[1,2,3,4,5], [3,4,5,1,2], 3],
        [[2,3,4], [3,4,3], -1],
        [[5], [4], 0],
        [[4], [5], -1],
        [[3,3,3,3,3,3,3,3], [5,1,4,4,4,2,2,2], 5],
        [[5,1,2,3,4], [4,4,1,5,1], 4],
        [[2], [2], 0],
    ])
    def test(self, nums1, nums2, exp_idx):
        s = Solution()
        act_idx = s.canCompleteCircuit(nums1, nums2)
        self.assertEqual(exp_idx, act_idx)