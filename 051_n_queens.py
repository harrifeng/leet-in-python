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
        return [["Q"]]
