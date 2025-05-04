import unittest
from typing import List

from parameterized import parameterized

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res_diff = 0
        met = {}
        for dom in dominoes:
            d_min = min(dom[0], dom[1])
            d_max = max(dom[0], dom[1])
            met[(d_min, d_max)] = met.get((d_min, d_max), 0) + 1
        for k, v in met.items():
            res_diff += v * (v-1) / 2
        return int(res_diff)


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[[1,2],[2,1],[3,4],[5,6]], 1],
        [[[1,2],[1,2],[1,1],[1,2],[2,2]], 3],
        [[[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]], 4],
    ])
    def test(self, n, exp):
        s = Solution()
        act_n = s.numEquivDominoPairs(n)
        self.assertEqual(exp, act_n)

