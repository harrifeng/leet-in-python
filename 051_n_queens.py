"""
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens'
placement, where 'Q' and '.' both indicate a queen and an empty space
respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

import unittest


class MyTest(unittest.TestCase):

    def test(self):
        solution = Solution()
        self.assertEqual([['.Q..', '...Q', 'Q...', '..Q.'],
                          ['..Q.', 'Q...', '...Q', '.Q..']],
                         solution.solveNQueens(4))
        self.assertEqual([['Q....', '..Q..', '....Q', '.Q...', '...Q.'],
                          ['Q....', '...Q.', '.Q...', '....Q', '..Q..'],
                          ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'],
                          ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'],
                          ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'],
                          ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'],
                          ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'],
                          ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'],
                          ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'],
                          ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']],
                         solution.solveNQueens(5))


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        tmp = ['.' * n for i in range(n)]
        self.helper(n, 0, tmp, ret)
        return ret

    def helper(self, n, level, tmp, ret):
        if level == n:
            ret.append(tmp[:])
            return
        for i in range(n):
            new_row = '.' * n
            tmp[level] = new_row[:i] + 'Q' + new_row[i + 1:]
            if self.is_valid(tmp, level, i):
                self.helper(n, level + 1, tmp, ret)
            tmp[level] = new_row

    def is_valid(self, board, row, col):
        for i in range(row):
            for j in range(len(board[0])):
                if board[i][j] == 'Q' and (j == col or
                                           abs(row - i) == abs(col - j)):
                    return False
        return True
