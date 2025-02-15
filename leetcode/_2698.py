import unittest
from functools import cache

from parameterized import parameterized

@cache
def is_punishment(i):
    def helper(s, acc, target):
        if s == "":
            return acc == target
        else:
            j = 0
            res = False
            while j < len(s):
                new_acc = acc + int(s[:(j + 1)])
                res = res or helper(s[(j + 1):], new_acc, target)
                j += 1
            return res

    sq = i * i
    sq_s = str(sq)

    return helper(sq_s, 0, i)


class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        i = 0
        while i <= n:
            if is_punishment(i):
                res += i * i
            i += 1
        return res


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [10, 182],
        [37, 1478],
    ])
    def test(self, nums1, exp_nums):
        s = Solution()
        act_n = s.punishmentNumber(nums1)
        self.assertEqual(exp_nums, act_n)

