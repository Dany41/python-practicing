import unittest
from typing import List

from parameterized import parameterized


def visit(grid, visited, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j]:
        return
    else:
        visited[i][j] = True

    if grid[i][j] == "1":
        visit(grid, visited, i+1, j)
        visit(grid, visited, i-1, j)
        visit(grid, visited, i, j+1)
        visit(grid, visited, i, j-1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        visited = [[False for b in range(m)] for r in range(n)]
        i = 0
        while i < n:
            j = 0
            while j < m:
                if grid[i][j] == "1" and not visited[i][j]:
                    visit(grid, visited, i, j)
                    res += 1
                j += 1
            i += 1
        return res


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ], 1],
        [[
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ], 3],
    ])
    def test(self, n, exp):
        s = Solution()
        act_n = s.numIslands(n)
        self.assertEqual(exp, act_n)

