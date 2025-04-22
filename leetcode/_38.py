import unittest
from typing import List

from parameterized import parameterized


def count_and_say_helper(s):
    new_str = ""
    n = len(s)
    if n == 1:
        return "1" + str(s[0])
    i = 1
    last_changed = 0
    curr = s[0]
    while i < n:
        if s[i - 1] != s[i]:
            l = i - last_changed
            new_str += str(l) + curr
            last_changed = i
            curr = s[i]
        i += 1

    if last_changed != i:
        new_str += str(i - last_changed) + curr

    return new_str


class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        res = "1"
        while i < n:
            res = count_and_say_helper(res)
            i += 1
        return res


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [1, "1"],
        [2, "11"],
        [3, "21"],
        [4, "1211"],
    ])
    def test(self, n, exp):
        s = Solution()
        act_n = s.countAndSay(n)
        self.assertEqual(exp, act_n)

