import unittest
from typing import List

from parameterized import parameterized


def scan_island(board, i, j, meta, island, visited):
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in island and board[i][j] == 'O':
        island.add((i, j))
        visited.add((i, j))
        meta[0] = min(meta[0], i)
        meta[1] = min(meta[1], j)
        meta[2] = max(meta[2], i)
        meta[3] = max(meta[3], j)
        scan_island(board, i + 1, j, meta, island, visited)
        scan_island(board, i, j + 1, meta, island, visited)
        scan_island(board, i - 1, j, meta, island, visited)
        scan_island(board, i, j - 1, meta, island, visited)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        i = 0
        n = len(board)
        m = len(board[0])
        visited = set()
        while i < n:
            j = 0
            while j < m:
                if board[i][j] == 'O' and (i, j) not in visited:
                    meta = [n, m, -1, -1] # top, left, bottom, right
                    island = set()
                    scan_island(board, i, j, meta, island, visited)
                    if meta[0] != 0 and meta[1] != 0 and meta[2] != n-1 and meta[3] != m-1:
                        for i1, j1 in island:
                            board[i1][j1] = 'X'
                j += 1
            i += 1



class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [
            [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
            [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        ],
        [
            [["X"]],
            [["X"]]
        ],
    ])
    def test(self, before, after):
        s = Solution()
        s.solve(before)
        self.assertEqual(before, after)

